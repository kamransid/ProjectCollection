#Update Package
apt update 
#Upgrade Package
apt upgrade 

#Basic Linux stuff
apt install -y git
#Apache
apt install -y apache2
#Enable apache mods
a2enmod rewrite

#Add Onrej PPA Repo
apt-add-repository ppa:ondrej/php
apt-get update

#Install PHP
apt-get install -y php7.2

#PHP Apache mod
apt-get install -y libapache2-mod-php7.2

#Restart Apache 
service apache2 restart 

#PHP Modules
apt-get install -y php7.2-common
apt-get install -y php7.2-mcrypt
apt-get install -y php7.2-zip

#Set MySql Pass
debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'


#Install MySql
apt-get install -y mysql-server

#PHP-MYSQL lib
apt-get install -y php7.2-mysql

#restart Apache
sudo service apache2 restart


