from kafka import KafkaConsumer
from json import loads, dumps
import logging
import requests

CONNECTION_SVC_ENDPOINT = "http://10.43.99.24:5000/"

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")

def consumeLocation():
    consumer = KafkaConsumer(
    'locations',
     bootstrap_servers=['udaconnect-kafka.default.svc.cluster.local:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     value_deserializer=lambda x: loads(x.decode('utf-8')))

    for message in consumer:
        logger.warning(f"reading location from kafka {message.value}")
        location = message.value
        res = requests.post(CONNECTION_SVC_ENDPOINT + "api/locations", json=location)
        logger.warning("done commiting to database",res.json())

consumeLocation()