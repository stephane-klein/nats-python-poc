#!/usr/bin/env python3
import datetime
import asyncio
import nats

async def publish():
    nc = await nats.connect("localhost")
    js = nc.jetstream()

    await js.add_stream(name="sample-stream", subjects=["foo"])
    ack = await js.publish("foo", f"hello world {datetime.datetime.isoformat(datetime.datetime.now())}".encode())
    print(ack)
    await nc.close()


if __name__ == '__main__':
    asyncio.run(publish())
