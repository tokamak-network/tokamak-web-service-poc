# Tokamak Web Service PoC

## Planning
[Planning Document](https://docs.google.com/presentation/d/18nSOzgvrDsUZb36V0VLtWatB8jJCmhgX5dUBctVnkXo/edit?usp=sharing)
\*@onther.io required

## Installation

```
$git clone https://github.com/Onther-Tech/tokamak-web-service-poc
$cd tokamak-web-service-poc
$virtualenv venv && source venv/bin/activate
$pip install -r requirements.txt
```

### config.ini

```
[AWS]
AWS_ACCESS_KEY = <aws access key>
AWS_SECRET_KEY = <aws secret key>

[INSTANCE]
BASIC_IMAGE_ID = <basic image>

INSTANCE_TYPE = <instance type --> e.q. t2.small>
SECURITY_GROUP_ID = <security group id>
KEY_NAME = <aws's ssh key file name>

REGION_NAME = <Instance Region --> e.q. ap-northeast-1>

[SSH]
SSH_USERNAME = <instance username --> e.q. ubuntu>
SSH_PEMFILE = <.pem file name>

[SERVER]
DEBUG = <is debug flag>
SECRET_KEY = <server secret key>
USERNAME = <server username>
PASSWORD = <server password>

[DATABASE]
DATABASE = <database file name>
```

### .pem file

In order to run this server, you need .pem file. If you create .pem file by this server, it will be stored on .pem directory. 

## API
