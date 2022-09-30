#! /usr/bin/python3

from datetime import date
import nmap
import json 
   
# take the range of ports to 
# be scanned
begin = 60
end = 81
  
# assign the target ip to be scanned to
# a variable
target = '192.168.162.131'
   
# instantiate a PortScanner object
scanner = nmap.PortScanner()
today = date.today()
date = today.strftime("%d/%m/%Y")
# date = str(datetime.now("%d%m%Y"))
result = []
with open("ports.json", "a") as outfile:
  outfile.write(f" \n    {date} machine {target} \n")
   
for i in range(begin,end+1):
   
    # scan the target port
    res = scanner.scan(target,str(i))
   
    # the result is a dictionary containing 
    # several information we only need to
    # check if the port is opened or closed
    # so we will access only that information 
    # in the dictionary
    res1 = res['scan'][target]['tcp'][i]['product']    
    res = res['scan'][target]['tcp'][i]['state']
    if res != "closed":
      with open("ports.json", "a") as outfile:        
        print(f'port {i} is {res}, the service is {res1}.', file=outfile)
   
    # print(f'port {i} is {res}.')
myFile2= open("myFile1.txt", "w")
myFile2.seek(0)
myFile2.write("New content by using truncate() method")
myFile2.truncate()
myFile2= open("myFile1.txt", "r")
print(myFile2.read())
