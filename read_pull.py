import asyncio
import nats

async def read():
    nc = await nats.connect("localhost")
    js = nc.jetstream()

    sub = await js.pull_subscribe("foo", "bar")
    while True:
        try:
            msgs = await sub.fetch()
        except TimeoutError:
            continue

        print(f"Msg: {msgs[0].data.decode()}")
        await msgs[0].ack()

    await nc.close()


if __name__ == '__main__':
    asyncio.run(read())
