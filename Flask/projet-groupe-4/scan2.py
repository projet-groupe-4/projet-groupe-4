#! /usr/bin/python3
#Import des librairies pour l'application
from fileinput import filename
from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect


import nmap
import json
import os 
# Définir le Root et récupération des arguments en POST ou Get
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
# Déclaration de la fonction pour la récupération des variables et les envoyer au Template 
def home():
# Vérification de l'existence d'un formulaire dans le canal 
    if request.form:
# Récupération de la variable Host=adresse IP"
        id = str(request.form['id'])
# Lancer le nmap PortScanner() et l'affecter sur une variable
        nm = nmap.PortScanner()
# Lancer le scan de Host      
        nm.scan(id)

        for host in nm.all_hosts():
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())
            for proto in nm[host].all_protocols():
                print('----------')
                print('Protocol : %s' % proto)
                lport = nm[host][proto].keys()
                # lport.sort()
                for port in sorted(lport):
                    print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))  
# Renvoyer les résultats vers template     
        return render_template('home.html', host=id, etat=nm[host].state(),all_proto=nm[host].all_protocols(), proto=proto, lport=lport, port=port, lport2=sorted(lport), state=nm[host][proto][port]['state'] )
    return render_template('home.html')
breakpoint   


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8082)


