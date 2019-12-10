from aiohttp import web
import aiohttp_jinja2
from db import close_pg, init_pg
import jinja2
from middlewares import setup_middlewares
from routes import setup_routes
from settings import BASE_DIR, config

app = web.Application()
setup_routes(app)
setup_middlewares(app)
app["config"] = config
aiohttp_jinja2.setup(
    app, loader=jinja2.FileSystemLoader(str(BASE_DIR / "polls" / "templates"))
)
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
web.run_app(app)
