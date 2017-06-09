#!/usr/bin/env python3
# coding: utf-8

import asyncio
import logging
#  import os
#  import json
#  import time
from aiohttp import web

logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(content_type='text/html', body=b'<h1>Blog</h2>')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9999)
    logging.info('server started at http://127.0.0.1:9999...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
