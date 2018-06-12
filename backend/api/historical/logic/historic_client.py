from kafka_tfrx.stream import KafkaStream
from rx import Observer, Observable
import logging.config
from datetime import timedelta, datetime

logging.config.fileConfig('kryptoflow/serving/backend/logging.conf')
log = logging.getLogger(__name__)


def get_historic_data(offset, max_points=50000):
    stream = KafkaStream.avro_consumer(topic='gdax', offset=offset)
    source = Observable \
        .from_(stream) \
        .take_while(lambda value: datetime.now() -
                                  datetime.strptime(value['ts'], '%Y-%m-%d %H:%M:%S') > timedelta(seconds=5))

    a = source.to_blocking()
    return [msg for msg in a][-max_points:]


def format_data(payload):
    return [{k: v for k, v in i.items() if k in ['price', 'ts']} for i in payload]


if __name__ == '__main__':
    get_historic_data(1689841)
