import sys

from aiohttp import web

from .db import close_pg, init_pg
from .routes import setup_routes
from .settings import config


async def init_app(argv=None):
    app = web.Application()
    app["config"] = config
    setup_routes(app)
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)

    return app


def main(argv):
    app = init_app(argv)

    web.run_app(app)


if __name__ == "__main__":
    main(sys.argv[1:])
