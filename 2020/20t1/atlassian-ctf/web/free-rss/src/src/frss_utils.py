import requests
from lxml import etree
import io

"""
Validate URL
===

Bypassing URL Validation in order to use SSRF to scan internally is the first
major road bump in the challenge.

This SSRF is intended to require knowledge of DNS spoofing/rebinding.

There are 3 modes we can run this part of the challenge in, each of varying difficulty and novelty.
1. Blacklisting. We black list a set of common payloads, eventually requiring the user to use a generic
   DNS spoofing attack in order to achieve SSRF, for example this could be achieved with nip.io. This is
   the easiest method.          NOT IMPLEMENTED
2. Realistic. In this we whitelist a set of payloads that may normally be associated with RSS. One of these
   will be apple.com, as it is currently (Feb 2020) possible to use mail.apple.com.?? and resolve to
   127.0.0.1. This is slightly harder, but discourages ingenuity, and to an extent requires the player to
   know about the issue in advance. It is however much more realistic than the first option.
3. Rebinding. Instead of using spoofing, we instead require a DNS rebind. We similarly whitelist a set
   of realistic urls (e.g. apple.com), and check their IP addresses in order to validate them. This requires the
   attacker to rebind in order to trick the validation algorithm the first time. This is also rather realistic,
   but is much more challenging than spoofing.
"""
ALLOWED_URLS = [
    s.split('.') for s in (
        "apple.com",
        "apple.com.??",
        "itunes.com",
        "itunes.com.??"
    )
]

def validate_url(url):
    try:
        return _validate_url_real(url)
    except:
        return False

def validate_get_urls():
    return ", ".join(".".join(p) for p in ALLOWED_URLS)

def _validate_url_real(url):
    parsed = requests.utils.urlparse(url)
    host = parsed.hostname

    host = host.split('.')
    valid = False
    for allowed in ALLOWED_URLS:
        # Match backwards
        for i in range(len(allowed)):
            host_part = host[-(i+1)]
            allw_part = allowed[-(i+1)]

            if len(set(allw_part)) == 1 and allw_part[0] == '?':
                if len(host_part) != len(allw_part):
                    break
            elif host_part != allw_part:
                break
        else:
            valid = True

    return valid

def _validate_url_rebinding(url): return True
def _validate_url_blacklist(url): return True


"""
Get XML, gets the xml
"""
def get_xml(method, url, body):
    try:
        res = requests.request(method, url=url, data=body, allow_redirects=False)
        return res.content
    except Exception as e:
        return None

"""
Parse feed

This is the third and final part of the challenge.
Here we intentionally expose a XXE vulnerability, allowing the user to get arbitrary file read.
"""
def parse_feed(xml):
    try:
        parser = etree.XMLParser(load_dtd=True, resolve_entities=True)
        tree = etree.parse(io.BytesIO(xml), parser=parser)
        root = tree.getroot()
        ns   = root.nsmap

        title = tree.find('title', ns).text
        updated = tree.find('updated', ns).text
        feed_items = []

        for entry in tree.findall('entry', ns):
            feed_items.append({k: entry.find(k, ns).text for k in ('updated', 'title', 'content')})

        return title, updated, feed_items
    except Exception as e:
        print(e)
        return None
