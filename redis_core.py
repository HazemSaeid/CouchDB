import asyncio
import aioredis as rc


async def add_death():
    redis = await rc.create_redis_pool("redis://localhost:6379")

    data = await redis.get('covid_deaths', encoding="utf-8")
    if(data == None):
        redis.set("covid_deaths",0)
    else:
        redis.incr('covid_deaths')

    print(data)
    redis.close()
    await redis.wait_closed()
        

asyncio.run(add_death())