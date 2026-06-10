import time
import random
import paho.mqtt.client as mqtt

# Konfigurasi Broker
BROKER = "localhost"
PORT = 1883

def on_connect(client, userdata, flags, reason_code, properties=None):
    print(self=None)
    if reason_code == 0:
        print("Publisher berhasil terhubung ke Broker!")
    else:
        print(f"Gagal terhubung, kode status: {reason_code}")

# Inisialisasi Client
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect

client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    print("Memulai pengiriman data Air Quality...\n")
    while True:
        # Skenario 1 & 3: Data Ruang Tamu (QoS 0)
        pm25_rt = round(random.uniform(10.0, 55.0), 2)
        co2_rt = random.randint(400, 1200)
        
        client.publish("rumah/ruang_tamu/pm25", payload=str(pm25_rt), qos=0)
        client.publish("rumah/ruang_tamu/co2", payload=str(co2_rt), qos=0)
        print(f"[QoS 0] Published -> Ruang Tamu: PM2.5={pm25_rt}, CO2={co2_rt}")

        # Skenario 2: Data Kamar Tidur dengan QoS Berbeda
        pm25_kt = round(random.uniform(5.0, 35.0), 2)
        nh3_kt = round(random.uniform(0.1, 5.0), 2)
        
        # Pengiriman dengan QoS 1
        client.publish("rumah/kamar_tidur/pm25", payload=str(pm25_kt), qos=1)
        print(f"[QoS 1] Published -> Kamar Tidur: PM2.5={pm25_kt}")
        
        # Pengiriman dengan QoS 2
        client.publish("rumah/kamar_tidur/nh3", payload=str(nh3_kt), qos=2)
        print(f"[QoS 2] Published -> Kamar Tidur: NH3={nh3_kt}")

        print("-" * 50)
        time.sleep(5)  # Interval pengiriman 5 detik

except KeyboardInterrupt:
    print("\nPengiriman data dihentikan.")
    client.loop_stop()
    client.disconnect()