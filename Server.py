from scapy.all import *

def packet_handler(packet):
    if packet.haslayer(UDP) and packet.haslayer(Raw):
        data = packet[Raw].load.decode(errors="ignore")
        src_ip = packet[IP].src
        src_port = packet[UDP].sport

        print(f"\nReceived from {src_ip}:{src_port}")
        print("Data:", data)


print("Sniffing UDP packets... (Ctrl+C to stop)")
sniff(filter="udp", prn=packet_handler, store=0)
