# Manage  and monitor  SSL  Certificates with  CERT MAN V1

This project aims to manage and monitor SSL certificate lifecycle. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installation

This project can be  run with docker-compose and also manually run on a server which mysql and  python installed. 

Traditional Methods:

* Install Mysql
* Download Binaries
* Create Mysql user and  database
* Edit mysql configuration file under ./dashboard/settings.py
* Run python django
```
  - #pip install -r requirements.txt
  - #systemctl start  mysqld
  - #python manage.py migrate
  - #python manage.py runserver 0.0.0.0:8000
  - #curl  -s  -v  http://localhost:8000
 ```
Container Methods Prerequisites:
```
  - #mkdir /appdata/
  - #git clone https://github.com/yildirima/CertMan.git
  - #cd /appdata/CertMan
  - #docker-compose  up  --build
  - #curl  -s  -v  http://localhost:8000
```
### CertMan  Dashboard
![CertMan  Dashboard](https://user-images.githubusercontent.com/15966685/59183360-76604a80-8b74-11e9-82ec-abf0e01ce934.png)

