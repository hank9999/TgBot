import aiohttp
from Setting import TgSetting

async def SendMessage(text):
    data = {'chat_id': TgSetting['groupId'], 'text': text}
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.post('https://api.telegram.org/bot' + TgSetting['token'] + '/sendMessage', data=data):
            pass
