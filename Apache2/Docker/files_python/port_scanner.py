#! /usr/bin/python3
import nmap

nm = nmap.PortScanner()
nm.scan('192.168.245.129-135')

result = open("scan_port.txt", "a") 
for host in nm.all_hosts():
    result.write('----------------------------------------------------\n')
    result.write('Host : %s (%s)\n' % (host, nm[host].hostname()))
    result.write('State : %s\n' % nm[host].state())
    for proto in nm[host].all_protocols():
        result.write('----------\n')
        result.write('Protocol : %s\n' % proto)
        lport = nm[host][proto].keys()        
        for port in sorted(lport):
            result.write('port : %s\tstate : %s\n' % (port, nm[host][proto][port]['state']))
result.close()
                