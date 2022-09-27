#! /usr/bin/python3

def port_scanner():
  from datetime import datetime
  import nmap
  import json 
  # take the range of ports to 
  # be scanned
  begin = 21
  end = 81
    # assign the target ip to be scanned to
  # a variable
  target = '127.0.0.1'
    
  # instantiate a PortScanner object
  scanner = nmap.PortScanner()
  date = str(datetime.now())
  result = []
  with open("ports.json", "a") as outfile:
    outfile.write(f" \n    {date} machine {target} \n")
  for i in range(begin,end+1):   
      # scan the target port
      res = scanner.scan(target,str(i))
      # print(json.dumps(res, indent = 4))
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
      