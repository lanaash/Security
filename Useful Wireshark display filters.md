# Wireshark display filters

## WiFi
```
wlan.fc.type_subtype eq 12    # Deauth
wlan.fc.type_subtype eq 10    # Disassociate
wlan.bssid == [MAC]           # See traffic to AP (your own??)
```
## DNS
```
dns.qry.type == 1             # A record requests
dns.flags.response == 1       # Query response (request is 0)
dns.qry.name
(dns.flags.response == 0) and (ip.src == x.x.x.x)
```
## Pi-Hole
```
dns.a == 0.0.0.0
```
## HTTP Host header
```
http.host
```
## HTTP requests;
```
(http.request.method == GET) or (http.request.method == POST)
```
## HTTPS
```
tls.handshake.type == 1      # See server name in Extentions: server_name
tls.handshake.extensions_server_name
```
## Scanning
```
tcp.flags.syn==1 and tcp.flags.ack==0 and tcp.window_size > 1024    # TCP Connect 
tcp.flags.syn==1 and tcp.flags.ack==0 and tcp.window_size <= 1024   # TCP SYN
icmp.type==3 and icmp.code==3                                       # UDP
udp.dstport > 55 and udp.dstport < 77 and not icmp                  # UDP Open
```

## ARP
```
arp.opcode == 1                                          # Request
arp.opcode == 2                                          # Response
arp.src.hw_mac == 00:00:00:00:00:00 and arp.opcode == 1  # ARP Scan
```
## MAC
```
eth.addr == 00:00:00:00:00:00
eth.dst == 00:00:00:00:00:00 and http
```
## DHCP
```
dhcp.option.dhcp == 3                           # Request
dhcp.option.hostname contains "Galaxy"
```
## NetBIOS Name Service
```
nbns
nbns.name contains "LIVALJM"
```
## Data smuggling
```
dns
data.len > 64 and icmp
```
## NFS
```
nfs.names
nfs.opcode == 68
```
## FTP
```
ftp.response.code == 200         # Valid login
ftp.response.code == 530         # Invalid login
```
## HTTP
```
http.request
http.response
http.host contains "rad"
http.host matches "\.(php|html)"
http.server contains "Apache"
http.server contains "Microsoft-IIS/7.5"
http.user_agent                  # Add to columns!
http.request.full_uri == "http://cdn.blablabla.xyz:8080/27fe2489"
http.request.uri contains “.php”
```
## HTTP Abuse
```
(http.user_agent contains "sqlmap") or (http.user_agent contains "Nmap") or (http.user_agent contains "Wfuzz") or (http.user_agent contains "Nikto")
http.request.method ==GET and http.request.uri contains "OR"  # SQLi
http.request.method == POST or http.response == 302   # Succesful Brute Force - follow HTTP Stream back from the 302 to /account for example
```
## TCP
```
tcp.port in {80 443 8080}
```
## TCP SYNs e.g. MSS;
```
tcp.port == 443 and tcp.flags.syn == 1
```
## IP
```
ip.addr
ip.src
ip.dst
```
## IP fragmentation
ip.flags.mf == 1 or ip.frag_offset > 0
