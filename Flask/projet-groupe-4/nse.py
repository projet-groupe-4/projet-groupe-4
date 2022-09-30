#! /usr/bin/python3
#Import des liberairies pour l'application
from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect
# from nse import *
# import nmap
import sys
import os

app = Flask(__name__)
# Définir le Root et récupération des arguments en POST ou Get

@app.route('/', methods=['GET','POST'])


# Déclaration de la fonction pour la récupération des variables et les envoyer au Template
def home():
# Vérification de l'existance d'un formulaire dans le canal 
    if request.form:
# Récupération de la variable Host=adresse IP"
        id = request.form['id2']
# lancement des scan avec vulscan.nse
        nmap1 = 'sudo nmap -sV --script=scipag_vulscan/vulscan.nse'
        nmap2 = 'nmap --script default'
        var1 = os.system(f"{nmap1} {id} | tee ./static/files/nse1.txt")
        var2 = os.system(f"{nmap2} {id} | tee ./static/files/nse2.txt") 
# Renvoyer les résultats vers template    
        return render_template('home2.html', var1=var1, var2=var2 )
    return render_template('home2.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8082)




