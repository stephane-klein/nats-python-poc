Ressources:

- [NATS - Python3 Client for Asyncio](https://github.com/nats-io/nats.py)
- [Learn NATS by Example](https://natsbyexample.com/)

Install

```sh
$ curl -L --progress-bar \
    -o nats-0.0.35-amd64.rpm \
    https://github.com/nats-io/natscli/releases/download/v0.0.35/nats-0.0.35-amd64.rpm
$ sudo rpm -i nats-0.0.35-amd64.rpm
```

```
$ docker-compose up -d
```

```
$ nats server check
OK Connection OK:connected to nats://127.0.0.1:4222 in 1.069768ms OK:rtt time 130.604µs OK:round trip took 0.000188s | connect_time=0.0011s;0.5000;1.0000 rtt=0.0001s;0.5000;1.0000 request_time=0.0002s;0.5000;1.0000
```

```
$ nats sub ">"
```

```
$ nats pub hello worldaeiua
```

## Python walkthrough

```sh
$ pip install -r requirememts.txt
```

```
$ python read_pull.py
```

In another shell session:

```
$ python publish.py
```

Log:

```
Msg: hello world 2023-03-04T09:59:10.572252
```
