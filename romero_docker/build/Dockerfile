FROM  python:bullseye
#spécifier le répertoire de travail
WORKDIR /app
COPY files_python/. .

#installation des dependence
# installation de pip et nmap 
RUN apt update &&\ 
    apt-get install pip nmap -y
# maj de pip
RUN pip install --no-cache-dir --upgrade pip

# APACHE
RUN apt install apache2 -y
CMD apachectl -D FOREGROUND
EXPOSE 80

# PYTHON
# installation des modules python paramiko et python-nmap
RUN pip3 install paramiko==2.11.0 python-nmap==0.7.1

#lancement des scripts
COPY files_web/index.html /var/www/html/index.html
RUN python port_scanner.py
RUN python python.py
RUN cp scan_* /var/www/html/.