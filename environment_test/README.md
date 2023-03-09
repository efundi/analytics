# CentOS 7 Python installation #
 
## Instructions to install required OS packages:
<code>
sudo yum -y update

sudo yum install -y epel-release

sudo yum groups mark install

sudo yum -y install yum-utils

sudo yum -y groupinstall development

sudo yum install -y python36

</code>
 

## CentOS 7 pip and other packages installation
<code>
sudo yum install -y openssl-devel

sudo yum install libffi-devel

sudo yum install -y openssl-devel

sudo yum install python-pip

cd /opt/current

sudo git clone https://github.com/1EdTech/caliper-python.git 

pip3 install -e caliper-python

sudo git clone https://github.com/efundi/analytics.git 

cd analytics

git checkout main

cd environment_test

pip install -r requirements.txt

touch .env

nano .env
</code>

### Content of .env file, which is read when the test.py is run

<code>
DATABASE_URI=<DATABASE_SERVER_IP_ADDRESS_HERE>
DATABASE_NAME=<DATABASE_NAME_ADDRESS_HERE>
DATABASE_USERNAME=<DATABASE_USERNAME_HERE>
DATABASE_PASSWORD=<DATABASE_USERNAME_PASSWORD_HERE>
DATABASE_PORT=3306
PROXY_URL=<PROXY_URL_HERE>
TARGET_URI=159.69.42.76:9966
TARGET_NAME=OpenLRW
TARGET_USERNAME=b8e071a6-e853-45d1-b805-e78fe042df66
TARGET_PASSWORD=cdccd318-f487-48ae-bc82-56fe6eff4bc4
LOG_LOCATION=.
</code> 

## Run the test
<code>
python3 test.py
</code>

