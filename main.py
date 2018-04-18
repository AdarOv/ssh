from scapy.all import *
from scapy.utils import rdpcap
from scapy.layers.inet import TCP
path = './super-short-ssh.pcap'
with PcapReader(path) as reader:
    while True:
        for pck in reader:
            # pck[IP].src ='132.72.236.101'
            sendp(pck)
