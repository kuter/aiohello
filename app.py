import sys

from aiohttp import web

from polls.main import init_app


def main(argv):
    app = init_app(argv)

    web.run_app(app)


if __name__ == "__main__":
    main(sys.argv[1:])
