#! /usr/bin/python3
import paramiko

command = "df"

# sudo nmap -O -sV --script=smb-os-discovery.nse 192.168.245.129


# Update the next three lines with your
# server's information

host = "192.168.245.129"
username = "romero"

pkey=paramiko.RSAKey.from_private_key_file("/home/romero/projet_ansible/romero_python/id_rsa")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, pkey=pkey)
_stdin, _stdout,_stderr = client.exec_command("df")
client.exec_command("git clone https://github.com/vulmon/Vulmap-Local-Vulnerability-Scanners.git")
client.exec_command(f"""python3 '/home/romero/Vulmap-Local-Vulnerability-Scanners/Vulmap-Linux/vulmap-linux.py' | tee test""")
client.exec_command("print($a) > test.json")
print(_stdout.read().decode())
client.close()