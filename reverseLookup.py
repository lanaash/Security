import socket

ip_file = open('ips.txt', 'r')
temp = ip_file.read().splitlines()
for ip in temp:
    try:
        ip_lookup = socket.gethostbyaddr(ip)
        host = ip_lookup[0]
    except:
        host = 'unknown'
    print "{},{}".format(ip,host)
