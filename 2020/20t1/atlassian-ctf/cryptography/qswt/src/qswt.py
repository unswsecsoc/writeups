import urllib.parse
import binascii
import hashlib
from typing import Union, Optional

def get_hash(data: Union[str, bytes]) -> bytes:
	"""Utility function to generate SHA1 hash

    Arguments:
        data {Union[str, bytes]} -- data to hash

    Returns:
        bytes -- hash digest
    """
	s = hashlib.sha1()
	if type(data) == str:
		data = data.encode('ascii')
	s.update(data)
	return s.digest()

def encode(data: dict, secret: bytes) -> str:
    """Encode qswt

    Arguments:
        data {dict} -- data to encode
        secret {bytes} -- signing secret

    Returns:
        str -- qswt token
    """
    text = urllib.parse.urlencode(data).encode('ascii')
    digest = get_hash(secret + text)
    return binascii.hexlify(text).decode('ascii') + '.' + binascii.hexlify(digest).decode('ascii')

def decode(token: str, secret: bytes) -> Optional[dict]:
    """Decode qswt. Returns None if token is invalid or cannot be decoded.

    Arguments:
        token {str} -- encoded qswt token
        secret {bytes} -- signing secret

    Returns:
        Optional[dict] -- data contained within qswt
    """
    token = token.split('.')
    if len(token) != 2:
        return None

    text, digest = token
    try:
        text = bytearray.fromhex(text)
        digest = bytearray.fromhex(digest)
        if get_hash(secret + text) == digest:
            return dict(urllib.parse.parse_qsl(text.decode('ascii', 'ignore')))
        return None
    except Exception as e:
        print(e)
        return None