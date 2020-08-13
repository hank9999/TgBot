from libs.Message import ReplyMessage
from libs.List import List
from Setting import TgSetting


async def helpCommand(message_id):
    text = (
        '帮助:\n'
        '/say 发送消息至MC服务器\n'
        '/run 远程执行指令\n'
        '/list 列出服务器信息\n'
    )
    await ReplyMessage(text, message_id)


async def listCommand(message_id):
    text = await List()
    await ReplyMessage(text, message_id)


async def runCommand(text, message_id):
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
            elif text.find('/list') == 0:
                await listCommand(message_id)
            elif text.find('/run') == 0:
                await runCommand(text, message_id)
