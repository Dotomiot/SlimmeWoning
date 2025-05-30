from .Apparaten import *

class MQTT_topic():
    def __init__(self, topic):
        self.topic = topic
        self.subscribers: list[Apparaat] = []

    def subscribe(self, apparaat: Apparaat):
        self.subscribers.append(apparaat)
        apparaat.subscribe(self.topic)

    def publish(self, data):
        for apparaat in self.subscribers:
            apparaat.recieve_mqtt(self.topic, data)
