dsn = 'http://1f85da6a0cca43859bed9002e188eb0f:85d369b20bb047479079d68d1a9aa31b@127.0.0.1:9000/3'

from raven import Client

client = Client(dsn=dsn)

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()