import json
import requests
from libs.Encryption import encrypt, decrypt
from Setting import ClientServerUrl, ServerList


async def List():
    try:
        data = await encrypt(json.dumps(ServerList))
        r = requests.post(ClientServerUrl + '/list', data=data)
        if r.status_code != 200:
            return r.text
        result = await decrypt(r.text)
        return result
    except Exception:
        return '获取状态过程中出错'
