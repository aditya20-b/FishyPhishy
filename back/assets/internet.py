import aiohttp


class AsyncInternet:
    instance = None

    def __new__(cls):
        # this will be a singleton class
        if not hasattr(cls, 'instance'):
            cls.instance = super(AsyncInternet, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def get(self, url):
        async with self.session.get(url) as response:
            return await response.json()

    async def post(self, url, data):
        async with self.session.post(url, data=data) as response:
            return await response.json()

    async def close(self):
        await self.session.close()

