
import socket
from struct import *

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
except socket.error , msg:
	print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()

# receive a packet

packet = s.recvfrom(65565)
	
#packet string from tuple
packet = packet[0]
	
#take first 20 characters for the ip header
ip_header = packet[0:20]
	
#now unpack them :)
iph = unpack('!BBHHHBBH4s4s' , ip_header)
	

s_addr = socket.inet_ntoa(iph[8]);
d_addr = socket.inet_ntoa(iph[9]);
	
tcp_header = packet[21:21+20]

tcph = unpack('!HHLLBBHHH',tcp_header)
source_port = tcph[0]
dest_port = tcph[1]
sequence = tcph[2]
acknowledgement = tcph[3]

print ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)
print ' Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port)		