import re
from libs.MCRcon import MCRcon
from Setting import RconSetting


async def rcon(name, command):
    for k, v in RconSetting.items():
        if k == name:
            with MCRcon(v['address'], v['password'], v['port']) as mcr:
                r = mcr.command(command)
            r = re.sub('§[0-9a-fk-or]', '', r, re.IGNORECASE)
            return r
        else:
            return '不存在该子服的RCON配置, 请检查子服名称'
