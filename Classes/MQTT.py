from .Apparaten import *
from .Smarthub import Smarthub

from typing import Union

class MQTT_topic():
    def __init__(self, topic: str):
        self.topic = topic
        self.subscribers: list[Apparaat] = []

    def subscribe(self, apparaat: Union[Apparaat, Smarthub]):
        if apparaat is None:
            return
        self.subscribers.append(apparaat)
        apparaat.subscribe(self.topic)

    def publish(self, data):
        for apparaat in self.subscribers:
            apparaat.recieve_mqtt(self.topic, data)
