import json
import requests
from libs.Encryption import encrypt, decrypt
from Setting import ClientServerUrl


async def rcon(address, port, password, command):
    try:
        data = encrypt(json.dumps({'address': address, 'port': port, 'password': password, 'command': command}))
        r = requests.post(ClientServerUrl + '/rcon', data=data)
        if r.status_code != 200:
            return r.text
        result = decrypt(r.text)
        return result
    except Exception:
        return 'RCON执行过程中出错'
