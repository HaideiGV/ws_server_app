import asyncio
import time

from aiohttp import web, log, WSMsgType


async def ws_handler(request):
    log.ws_logger.info("WebSocket connection starting...")

    ws = web.WebSocketResponse(autoclose=False)
    await ws.prepare(request)

    users = request.app['users']
    users.append(ws)

    log.ws_logger.info("WebSocket connection ready.")

    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            log.ws_logger.info("Received message: ", msg.data)
            if msg.data == 'close':
                await ws.close()
            else:
                t1 = time.time()
                await asyncio.sleep(5)
                t2 = time.time()

                for user in users:
                    try:
                        await user.send_str(
                            f"Returned message: {msg.data}, after {t2 - t1}"
                        )
                    except Exception as e:
                        log.ws_logger.error(
                            f"Error was happened during broadcasting: {str(e)}",
                            exc_info=True
                        )
                log.ws_logger.info("Message was parsed.")
    return ws


def main():
    loop = asyncio.get_event_loop()
    app = web.Application(loop=loop)

    app['users'] = []
    app.router.add_routes([
        web.get("/", ws_handler)
    ])
    web.run_app(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
