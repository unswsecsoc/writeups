import random
import string
from flask import Flask, request, abort, Response
from subprocess import check_output
from base64 import b64encode

app = Flask(__name__)


@app.errorhandler(401)
def handler_401(_):
    return Response("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>401 Unauthorized</title>
<h1>Unauthorized</h1>
<p>Authentication is required to unseal TPM secrets</p>
""", 401, {'WWW-Authenticate': 'Basic'})


@app.route("/")
def route_index():
    return Response("""MIPS Management Engine v9.2
Copyright (c) 2018 MIPS Corporation <info@mipscorporation.com>

This product contains technologies that are patent pending.
This product may contain traces of spim.

See /help for documentation.
""", mimetype='text/plain')


@app.route("/info")
def route_info():
    return Response("""MIPS Management Engine v9.2
Copyright (c) 2018 MIPS Corporation <info@mipscorporation.com>

This product contains technologies that are patent pending.
This product may contain traces of spim.

See /help for documentation.
""", mimetype='text/plain')


@app.route("/help")
def route_help():
    return Response("""MIPS Management Engine v9.2
Copyright (c) 2018 MIPS Corporation <info@mipscorporation.com>

/info               Displays information about MIPS Management Engine
/help               Displays the current help document
/system/current_pc  Displays the current program counter of the processor
/tpm/info           Displays information about the Trusted Platform Module
""", mimetype='text/plain')


@app.route("/system/current_pc", methods=['GET'])
def route_system_current_pc():
    return Response(str(int(check_output("cat /proc/uptime | cut -d' ' -f1 | tr -d '.'", shell=True))) + "\n",
                    mimetype='text/plain')


@app.route("/tpm/info")
def route_tpm_info():
    return Response("""MIPS Management Engine v9.2
Copyright (c) 2018 MIPS Corporation <info@mipscorporation.com>

Infinity Trusted Platform Module v2.1
Copyright (c) 2018 Infinity Corporation <trustedcomputing@infinity.com>

/info               Displays TPM info
/list               List metadata of stored secrets
/unseal/{uuid}      Unseal and reveal stored secrets (requires authentication)
""", mimetype='text/plain')


@app.route("/tpm/list")
def route_tpm_list():
    return Response("""MIPS Management Engine v9.2
Copyright (c) 2018 MIPS Corporation <info@mipscorporation.com>

Infinity Trusted Platform Module v2.1
Copyright (c) 2018 Infinity Corporation <trustedcomputing@infinity.com>

UUID                                    Name            Timestamp
22c2ea9e-97b5-11e8-9eb6-529269fb1459    flag            Sat, 04 Aug 2018 07:09:26 +0000
""", mimetype='text/plain')


@app.route("/tpm/unseal/22c2ea9e-97b5-11e8-9eb6-529269fb1459")
def route_tpm_unseal():
    authenticate_user()

    return Response("""MIPS Management Engine v9.2
Copyright (c) 2018 MIPS Corporation <info@mipscorporation.com>

Infinity Trusted Platform Module v2.1
Copyright (c) 2018 Infinity Corporation <trustedcomputing@infinity.com>

22c2ea9e-97b5-11e8-9eb6-529269fb1459
""" + get_flag() + "\n", mimetype='text/plain')


def authenticate_user() -> None:
    if request.authorization is None:
        abort(401)

    if len(request.authorization.username) > 3:
        abort(400, description="Maximum username length is 3 alphanumeric characters")

    if request.authorization.username != "tpm":
        abort(403, description="Authentication username invalid")

    computed_response = b64encode(get_auth().encode())
    user_response = b64encode((request.authorization.username + ":" + request.authorization.password).encode())
    response_length = len(user_response)

    if not constant_strncmp(computed_response, user_response, response_length):
        abort(403, description="Authentication digest mismatch")


def constant_strncmp(a: str, b: str, length: int) -> bool:
    """Constant time strncmp function

We do not use Python's built in comparison function because it is
vulnerable to timing attacks.

This function will perform a comparison regardless of the length or match of the input strings.

This way, time taken to compare two strings is constant and it will prevent timing attacks.
"""

    dummy1 = random.choice(string.ascii_letters)
    dummy2 = random.choice(string.ascii_letters)
    volatile = False

    # Ensure length is pegged to the strings
    if length > len(a):
        length = len(a)

    if length > len(b):
        length = len(b)

    for i in range(0, length):
        # If index out of bounds
        if i + 1 > len(a) or i + 1 > len(b):
            if dummy1 == dummy2:
                volatile = not volatile

        if a[i] != b[i]:
            return False

    return True


def get_auth() -> str:
    with open("secrets/auth") as f:
        return f.read().strip()


def get_flag() -> str:
    with open("secrets/flag") as f:
        return f.read().strip()
