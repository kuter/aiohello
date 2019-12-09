import sys

from aiohttp import web

from .routes import setup_routes
from .settings import config


async def init_app(argv=None):
    app = web.Application()

    setup_routes(app)
    app["config"] = config

    return app


def main(argv):
    app = init_app(argv)

    web.run_app(app)


if __name__ == "__main__":
    main(sys.argv[1:])
