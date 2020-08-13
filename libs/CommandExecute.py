from libs.Message import SendMessage, ReplyMessage
from Setting import TgSetting
import datetime


async def helpCommand(message_id):
    text = (
        '帮助:\n'
        '/say 发送消息至MC服务器\n'
        '/run 远程执行指令\n'
        '/list 列出服务器信息'
    )
    await ReplyMessage(text, message_id)


async def parser(data):
    print(data)

    try:
        message_id = data['message']['message_id']
        is_bot = data['message']['from']['is_bot']
        text = data['message']['text']
        if str(data['message']['chat']['id']) == TgSetting['groupId']:
            need_execute = True
        else:
            need_execute = False
    except Exception:
        message_id = 0
        is_bot = False
        text = ''
        need_execute = False

    if need_execute:
        if not is_bot:
            if text.find('/help') == 0:
                await helpCommand(message_id)