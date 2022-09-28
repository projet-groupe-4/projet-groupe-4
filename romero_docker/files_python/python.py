#! /usr/bin/python3
import paramiko

command = "python3 /home/romero/Vulmap-Local-Vulnerability-Scanners/Vulmap-Linux/vulmap-linux.py"

# sudo nmap -O -sV --script=smb-os-discovery.nse 192.168.245.129

# Update the next three lines with your
# server's information

host = "192.168.245.129"
username = "romero"

pkey=paramiko.RSAKey.from_private_key_file("id_rsa")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, pkey=pkey)
client.exec_command("git clone https://github.com/vulmon/Vulmap-Local-Vulnerability-Scanners.git")
_stdin, _stdout,_stderr = client.exec_command(command)
with open("scan_vulmap.txt", "w") as result:
    result.write(_stdout.read().decode().rstrip())
client.close()