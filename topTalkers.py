import sys
import re

logfile = sys.argv[1]

ips = dict()
log = open(logfile, "r")
for line in log:
    line = line.strip()
    ip = re.search('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
    if ip.group(1) in ips:
        ips[ip.group(1)] = ips[ip.group(1)] + 1
    else:
        ips[ip.group(1)] = 1

for key in list(ips.keys()):
    print(key, ":", ips[key])
