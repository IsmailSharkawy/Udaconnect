import logging
from datetime import datetime, timedelta
from typing import Dict, List
from kafka import KafkaProducer
import json
from json import dumps
import datetime

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")


producer = KafkaProducer(
    bootstrap_servers=["udaconnect-kafka.default.svc.cluster.local:9092"],
    api_version=(0, 11, 5),
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
)
topic = "locations"


class LocationProducer:
    @staticmethod
    def create_location(location: Dict):
        location["creation_time"] = datetime.datetime.now().isoformat()
        producer.send(topic, location)
