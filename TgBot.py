from aiohttp import web
import json
from libs.CommandExecute import parser
from Setting import WebServerSetting

routes = web.RouteTableDef()

@routes.get('/')
async def get_handler(request):
    return web.Response(text='Python Robot Server is running')


@routes.post('/' + WebServerSetting['post'])
async def post_handler(request):
    data = json.loads(await request.json())
    await parser(data)
    return web.Response(text='OK')


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host=WebServerSetting['host'], port=WebServerSetting['port'])
