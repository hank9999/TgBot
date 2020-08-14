from libs.Message import ReplyMessage
from libs.Rcon import rcon
from libs.List import List
from Setting import TgSetting, RconSetting


async def helpCommand(message_id):
    text = (
        '帮助:\n'
        '/say 发送消息至MC服务器\n'
        '/run 远程执行指令\n'
        '/list 列出服务器信息\n'
    )
    await ReplyMessage(text, message_id)
    return


async def listCommand(message_id):
    text = await List()
    await ReplyMessage(text, message_id)
    return


async def runCommand(message, message_id):
    if message.find('/run help') == 0:
        text = (
            '/run 帮助:\n'
            '/run help 获取帮助\n'
            '/run list 查看可用rcon子服\n'
            '/run <服务器名称> <指令>'
        )
        await ReplyMessage(text, message_id)
        return
    if message.find('/run list') == 0:
        text = ''
        for i in RconSetting.keys():
            text += str(i) + '\n'
        await ReplyMessage(text, message_id)
        return
    try:
        args = message[5:]
        servername = args[:args.find(' ')]
        command = args[args.find(' ')+1:]
    except Exception:
        text = '参数不全, 请使用 /run help 查看帮助'
        await ReplyMessage(text, message_id)
        return

    if args == '' or servername == '' or command == '':
        text = '参数不全, 请使用 /run help 查看帮助'
        await ReplyMessage(text, message_id)
        return

    rcon_info = {}
    for k, v in RconSetting.items():
        if servername.lower() == str(k).lower():
            rcon_info = v
    if rcon_info == {}:
        text = '不存在此子服 请执行 /run list 查看可用rcon子服'
        await ReplyMessage(text, message_id)
        return

    text = await rcon(rcon_info['address'], rcon_info['port'], rcon_info['password'], command)
    await ReplyMessage(text, message_id)
    return


async def sayCommand(message, message_id):
    if message.find('/say help') == 0:
        text = (
            '/say 帮助:\n'
            '/say help 获取帮助\n'
            '/say list 查看可用子服\n'
            '/say <服务器名称> <名称> <内容>'
        )
        await ReplyMessage(text, message_id)
        return
    if message.find('/say list') == 0:
        text = ''
        for i in RconSetting.keys():
            text += str(i) + '\n'
        await ReplyMessage(text, message_id)
        return
    try:
        args = message[5:]
        servername = args[:args.find(' ')]
        name_texts = args[args.find(' ')+1:]
        name = name_texts[:args.find(' ')-1]
        texts = name_texts[args.find(' '):]
    except Exception:
        text = '参数不全, 请使用 /say help 查看帮助'
        await ReplyMessage(text, message_id)
        return

    if args == '' or servername == '' or name_texts == '' or name == '' or texts == '' or name_texts.find(' ') < 0:
        text = '参数不全, 请使用 /run help 查看帮助'
        await ReplyMessage(text, message_id)
        return

    rcon_info = {}
    for k, v in RconSetting.items():
        if servername.lower() == str(k).lower():
            rcon_info = v
    if rcon_info == {}:
        text = '不存在此子服 请执行 /say list 查看可用子服'
        await ReplyMessage(text, message_id)
        return

    command = 'tellraw @a {"extra":[{"text":"§a"},{"clickEvent":{"action":"suggest_command","value":"[TG]' + name + '"},"text":"§f[TG] ' + name + '§r: "},{"text":"§f"},{"text":"§f' + texts + '"}],"text":""}'
    await rcon(rcon_info['address'], rcon_info['port'], rcon_info['password'], command)
    await ReplyMessage('已发送', message_id)
    return


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
            elif text.find('/say') == 0:
                await sayCommand(text, message_id)
