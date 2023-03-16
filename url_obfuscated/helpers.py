from django.conf import settings
from Crypto.Cipher import AES
import binascii

def generate_url_pattern(url, params=[], leaf=True):
    url_array = url.split('/')
    url_array = [url_fragment for url_fragment in url_array if url_fragment != '']

    response_array = []

    for url_fragment in url_array:
        response_array.append(obfuscate(url_fragment))

    response = str()
    if len(response_array) > 0:
        response = '/'.join(str(_) for _ in response_array)

    if params:
        for arg in params:

            response = '{0}/{1}'.format(response, arg)

    if len(response_array) > 0:
        if not response.endswith('/') and not response.endswith('?'):
            response = '{0}/'.format(response)

    if leaf:
        response = '{0}$'.format(response)

    return r'^' + response

def _pad(secret, blocksize=16, padding=' '):
    """Adds Padding if Secret Key is not of Legal AES Block Size ie. 16, 24, 32"""
    if not len(secret) in (16, 24, 32):
        return secret + (blocksize - len(secret)) * padding
    return secret

def obfuscate(value):
    secret = _pad(settings.SECRET_KEY[0:16])
    encrypt_obj = AES.new(secret)

    value = str.encode(value)
    value = str(value, 'utf-8')
    value = value + (' ' * (16 - (len(value) % 16)))
    encrypted = encrypt_obj.encrypt(value)
    hex_value = binascii.hexlify(encrypted)
    response = str(binascii.b2a_base64(hex_value)[:-1]).replace('+', '-').replace('/', '_').replace('=', '')
    response = response[2:-1]
    return response

def deobfuscate(value):
    secret = _pad(settings.SECRET_KEY[0:16])
    encrypt_obj = AES.new(secret)

    value = str.encode(value)
    value = str(value, 'utf-8')
    value = value.replace('-', '+').replace('_', '/')
    value = value + ('=' * (16 - (len(value) % 16)))
    decoded = binascii.a2b_base64(value).decode("utf-8")
    unhex = binascii.unhexlify(decoded)
    response = encrypt_obj.decrypt(unhex).rstrip()
    response = str(response, 'utf-8')
    return response
