import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *

infile= "file.pcap"

try:
	my_reader = PcapReader(infile)
	for p in my_reader:
		sendp(p)
except IOError:
	print "Failed to read %s " % infile
	sys.exit(1)