from scapy.all import *
from scapy.utils import rdpcap
from scapy.layers.inet import TCP
from scapy.layers.inet import IP

sport = random.randint(1024,65535)
dst= '132.72.81.37'
src = '132.73.198.238'
# SYN
ip = IP(dst=dst)
SYN=TCP(sport=sport,dport=22,flags='S',seq=1000)
SYNACK=sr1(ip/SYN)

# SYN-ACK
ACK=TCP(sport=sport, dport=22, flags='A', seq=SYNACK.ack + 1, ack=SYNACK.seq + 1)
send(ip/ACK)
