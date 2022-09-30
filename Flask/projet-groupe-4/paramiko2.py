#! /usr/bin/python3
#Import des librairies pour l'application
from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect
import paramiko
import sys
import os


app = Flask(__name__)

# Définir le Root et récupération des arguments en POST ou Get
@app.route('/', methods=['GET','POST'])

# Déclaration de la fonction pour la récupération des variables et les envoyer au Template 
def home():
# Vérification de l'existence d'un formulaire dans le canal 
    if request.form:
# Récupération de la variable Host=adresse IP"
        host = request.form['id3']
# Execution de Vulmap sous Linux
        command = "python3 './Vulmap-Local-Vulnerability-Scanners/Vulmap-Linux/vulmap-linux.py'"
        username = "mboufe"
# Paramiko: Récupération de la clé et l'utilisateur de la machine distante
        pkey=paramiko.RSAKey.from_private_key_file("projet-groupe-4")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, pkey=pkey)
        _stdin, _stdout,_stderr = client.exec_command("command")
# Un git clone de Vulnerability-Scanners
        client.exec_command("git clone https://github.com/vulmon/Vulmap-Local-Vulnerability-Scanners.git")
        client.exec_command(command)
        client.exec_command("print($a) > File_Paramiko.json")
        with open("./static/css/File_Paramiko.txt", "w") as result:
            result.write(_stdout.read().decode().rstrip())
            client.close()
# Renvoyer les résultats vers template            
            return render_template('home3.html', result=("File_Paramiko.txt") )
    return render_template('home3.html')





if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8082)