from flask import Flask, render_template, request, Markup
import json
import dateutil.parser
import requests
import datetime
import string
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == "POST":

            request_string = request.form.get("input", "")

            correct = (
                not request_string.isupper()
                and request_string.lower().count("gimme") == 30
                and after_midnight()
            )

            if correct:
                reply = Markup(
                    "<h3>Okay! Okay! Fine! Here's your man! "
                    "uh... I mean flag!:</br>"
                    "FLAG{&_!_g4z3_1nt0_th3_n!ght}</h3>"
                )
            else:
                reply = reply_to_request(request_string)

            with open("log.txt", "a", encoding="utf8") as log:
                time = datetime.datetime.now().isoformat()
                ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
                print(
                    f"{time} @ {ip}: {request_string} -> {reply}", file=log)

            return render_template('base.html', reply=reply, string=request_string)

        else:
            return render_template('base.html', reply="", string="")

    except Exception:
        return "Sorry, something broke (probably emoji). Otherwise, please contact evan@unswsecurity.com if this persists"

def dawn_from_location(location):
    lat, lng = location
    date = datetime.date.today().isoformat()
    url = (
         "https://api.sunrise-sunset.org/json?"
        f"lat={lat}&"
        f"lng={lng}&"
        f"date={date}&"
         "formatted=0"
    )
    r = requests.get(url)
    j = json.loads(r.text)
    dawn = j.get("results", {}).get("civil_twilight_begin", {})
    return dateutil.parser.parse(dawn).astimezone()

def after_midnight():
    unsw = (-33.9173, 151.2313)
    dawn = dawn_from_location(unsw)
    midnight = datetime.datetime.now().replace(
        hour=0, minute=0, second=0, microsecond=0
    ).astimezone()
    now = datetime.datetime.now().astimezone()
    print(midnight, now, dawn)
    return midnight < now < dawn

def multi_count(string, elements):
    return sum(
        string.count(element)
        for element in elements
    )

def reply_to_request(request):
    phrases = ("please", "plz", "pls", "plox", "plx")
    negative = (
        "no", "no.", "NO",
        "No.", "No", "no no", "no, no, no!",
        "no no no", "yes?", "yeah nah"
    )
    try_hard = (
        "Okay now you're just a try-hard",
        "Trrryyy Haaarrrdd",
        "Have you tried, tring harder?",
        "Try harder?",
        "Try harder!",
        "Where are *you* going in life?",
        "Seriously...",
        "Hey stop it!",
        "Hehe, it tickles",
        "Uhm...",
        "Despair",
        "This gets worse and worse, until you give up or die",
        ":)",
        "",
    )

    if not request:
        return ""

    if request.isupper():
        return "WHY ARE YOU SHOUTING AT ME?!"
    else:
        request = request.lower()

    if request.endswith("?"):
        if any(
            phrase in request
            for phrase in ("please", "plz", "pls", "plox", "pl0x")
        ):
            return "yes"
        else:
            return "Where's your manners?!"
    else:
        request = request.translate(str.maketrans("","",string.punctuation))

    with open("lyrics.txt") as lyrics_file:
        lines = [
            line.strip().lower().translate(str.maketrans("","",string.punctuation))
            for line in lyrics_file
        ]
        next_line = dict(zip(lines, lines[1:]))

    if request in next_line:
        return next_line[request] + " 🎶"

    if multi_count(request, phrases) == 2:
        return "Wow you're such a pushover"

    if 3 <= multi_count(request, phrases) < 100:
        return "Gee wish I could say please a hundred times and get whatever I wanted"

    if multi_count(request, phrases) >= 100:
        return "Okay now you just went too far..."

    if any(
        phrase in request
        for phrase in phrases
    ):
        return "I'll think about it"

    if request == " ":
        return "🌌"

    if "fuck" in request or "evan" in request:
        return "Listen here you little shit"

    if "gimmie" in request:
        return "What are you? Illiterate?"

    if "hey gimme that" in " ".join(request.split()):
        return "What are you? The Loot Hoarder?"

    if "hey" in request:
        return "Aren't you meant to be getting a flag or something?"

    if "i need it" in " ".join(request.split()):
        return "You definitely don't need it"

    if "flag" in request:
        return "This one 🇸🇪?"

    if "man" in request:
        return "Okay here, the best dressed man I could find 🕴"

    if "help" in request or "halp" in request:
        return "Don't ask me for help! You're meant to be helping Agnetha!"

    if "hint" in request:
        return "You want a hint already? -.-\" I'll give you one later... maybe..."

    count = request.count("gimme")
    if count == 1:
        return random.choice(negative)

    if count == 2:
        return "I said no!"

    if count == 3:
        return "okay, maybe..."

    if 3 < count < 10:
        return "maybe..."

    if count == 10:
        return "What on earth are you doing?"

    if count == 11:
        return "No, like staph"

    if count == 12:
        return "Seriously..."

    if count == 12:
        return "Okay whatever then"

    if 12 < count < 23:
        return random.choice(negative)

    if count == 23:
        return "I said maybe..."

    if count == 24:
        return "...you're gonna be the one that saves me..."

    if count == 25:
        return "You know, there is logic to this madness"

    if 25 < count < 29:
        return random.choice(negative)

    if count == 29:
        return "That number of gimmes is too damn high"

    if count == 30:
        return "DO YOU THINK SHE STUTTERED?!?!"
        return 'What part of "after midnight" did you not understand?'

    if count == 31:
        return "Thirty one"

    if (count & (count - 1)) == 0 and count:
        return "Indeed that is a power of 2"

    if 97 <= count <= 99:
        return (
            f"{count} containers of flags on the wall, "
            f"{count} containers of flags. "
             "Take one down and pass it around, "
            f"{count - 1} containers of flags on the wall...."
        )

    if count == 100:
        return "You probably won't reach that age"

    if count > 32:
        return random.choice(try_hard)

    return random.choice(negative)

    return (
        "Wow... Look at you... You managed to find an edge case after like 35"
        "different if statements... Go buy a lottery ticket..."
    )

if __name__ == '__main__':
    # you should be using this to debug. This allows you to attach an actual debugger to
    # your script, and you can see any errors that occurred in the command line. No pesky
    # log files like cgi does Also note that since use_reloader is on, you shouldn't make
    # changes to the code while the app is paused in a debugger, because it will reload as
    # soon as you hit play again
    app.run(debug=True, use_reloader=True, port=5555)

