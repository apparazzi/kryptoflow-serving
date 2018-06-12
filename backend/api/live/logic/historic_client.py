from kafka_tfrx.stream import KafkaStream

def get_live_data():
    a = KafkaStream(topic='gdax')
    msgs = a.read_new()
    if len(msgs) > max_points:
        return msgs[max_points:]
    return msgs


def format_data(payload):
    return [{k: v for k, v in i.items() if k in ['price', 'ts']} for i in payload]

