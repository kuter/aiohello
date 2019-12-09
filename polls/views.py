from aiohttp import web

from .db import question


async def index(request):
    async with request.app["db"].acquire() as conn:
        cursor = await conn.execute(question.select())
        records = await cursor.fetchall()
        questions = [dict(q) for q in records]
        return web.Response(text=str(questions))
