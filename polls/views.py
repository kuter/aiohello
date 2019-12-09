import aiohttp_jinja2

from .db import question


@aiohttp_jinja2.template("index.html")
async def index(request):
    async with request.app["db"].acquire() as conn:
        cursor = await conn.execute(question.select())
        records = await cursor.fetchall()
        questions = [dict(q) for q in records]
        return {"questions": questions}
