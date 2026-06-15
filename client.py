from scapy.all import *

# Destination details
target_ip = "127.0.0.1"
target_port = 12345

while True:
    msg = input("Enter message (type 'exit' to stop): ")

    if msg.lower() == "exit":
        break

    # Build UDP packet
    packet = IP(dst=target_ip) / UDP(dport=target_port) / Raw(load=msg)

    # Send packet
    send(packet)

    print("Packet sent!")
