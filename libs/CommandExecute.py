from libs.SendMessage import SendMessage
import datetime


async def helpCommand(username):
    message = (
        '@' + username + '帮助:\n'
        '/say 发送消息至MC服务器\n'
        '/run 远程执行指令\n'
        '/list 列出服务器信息'
    )
    await SendMessage(message)


async def parser(data):
    print(data)

    username = data['message']['from']['username']
    is_bot = data['message']['from']['is_bot']
    text = data['message']['text']
    if not is_bot:
        if text.find('/help') == 0:
            await helpCommand(username)
        else:
            pass
    else:
        pass
