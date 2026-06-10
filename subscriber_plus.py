import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC_PLUS = "rumah/+/pm25"

def on_connect(client, userdata, flags, reason_code, properties=None):
    print(f"Connected with result code: {reason_code}")
    # Subscribe ke wildcard single-level
    client.subscribe(TOPIC_PLUS)
    print(f"Subscribed ke topik: {TOPIC_PLUS}")

def on_message(client, userdata, msg):
    print(f"[WILDCARD +] Terima Pesan pada Topik: {msg.topic} -> Data: {msg.payload.decode()} (QoS: {msg.qos})")

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

print("Menunggu data dari Wildcard Plus (+)...")
client.loop_forever()