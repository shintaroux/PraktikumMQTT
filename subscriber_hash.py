import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC_HASH = "rumah/#"

def on_connect(client, userdata, flags, reason_code, properties=None):
    print(f"Connected with result code: {reason_code}")
    # Subscribe ke wildcard multi-level
    client.subscribe(TOPIC_HASH)
    print(f"Subscribed ke topik: {TOPIC_HASH}")

def on_message(client, userdata, msg):
    print(f"[WILDCARD #] TOTAL MONITORING -> {msg.topic} : {msg.payload.decode()} (QoS: {msg.qos})")

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

print("Menunggu semua data masuk via Wildcard Hash (#)...")
client.loop_forever()