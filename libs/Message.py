import json
from Setting import TgSetting, SendMode, ApiUrl


async def SendMessage(text, session):
    if SendMode == 1:
        data = json.dumps({'token': TgSetting['token'], 'jsonData': {'chat_id': TgSetting['groupId'], 'text': text}})
        session.post(ApiUrl, data=data, timeout=60, headers={'Content-Type': 'application/json'})
    else:
        data = json.dumps({'chat_id': TgSetting['groupId'], 'text': text})
        session.post(ApiUrl + '/bot' + TgSetting['token'] + '/sendMessage', data=data, timeout=60, headers={'Content-Type': 'application/json'})

async def ReplyMessage(text, reply_message_id, session):
    if SendMode == 1:
        data = json.dumps({'token': TgSetting['token'], 'jsonData': {'chat_id': TgSetting['groupId'], 'text': text, 'reply_to_message_id': reply_message_id}})
        session.post(ApiUrl, data=data, timeout=60, headers={'Content-Type': 'application/json'})
    else:
        data = json.dumps({'chat_id': TgSetting['groupId'], 'text': text, 'reply_to_message_id': reply_message_id})
        session.post(ApiUrl + '/bot' + TgSetting['token'] + '/sendMessage', data=data, timeout=60, headers={'Content-Type': 'application/json'})
