#! /usr/bin/python3
import nmap

nm = nmap.PortScanner()
nm.scan('192.168.245.125-131')


for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)
        lport = nm[host][proto].keys()        
        for port in sorted(lport):
            print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))