async def test_index(cli, loop):
    resp = await cli.get("/")
    assert resp.status == 200
    text = await resp.text()
    assert "Hello Aiohttp!" in text
