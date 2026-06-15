from scapy.all import *

target_ip = "127.0.0.1"
target_port = 12345

while True:
    msg = input("Enter message (type 'exit' to stop): ")

    if msg.lower() == "exit":

    packet = IP(dst=target_ip) / UDP(dport=target_port) / Raw(load=msg)
\
    send(packet)

    print("Packet sent!")
