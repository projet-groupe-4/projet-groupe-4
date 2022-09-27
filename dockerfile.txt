FROM python3:latest
#spécifier le répertoire de travail
WORKDIR /home/user
#installation des dépendances
vulmap==2.2
paramiko==
#copier les dépendances dans un fichier
COPY dependance.txt .
#installe les dépendances dans le fichier et supprime le fichier par la suite
RUN pip install -r dependance.txt && rm requirements.txt

#lancement des scripts
ENTRYPOINT ["python", "port_scanner.py"]
ENTRYPOINT ["python", "scan.py"]
ENTRYPOINT ["python", "python.py"]