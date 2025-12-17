My sql database setup 



Step 1 - 

(Optional) pull the official image:

docker pull mysql:8.0



Step 2- 

**docker run --name mysql -e MYSQL\_ROOT\_PASSWORD=rootpass -e MYSQL\_DATABASE=mydb -e MYSQL\_USER=myuser -e MYSQL\_PASSWORD=mypass -p 3300:3306 -v mysql-data:/var/lib/mysql -d mysql:8.0**



put port/password/database name according to your requirements.



step 3- 

Status check

**docker ps**

\# or

**docker port mysql**

\# example output: 0.0.0.0:3300->3306/tcp



step 4- 

Connect from inside the container

docker exec -it mysql mysql -uroot -p

\# when prompted enter: rootpass

\# or connect as the non-root user:

docker exec -it mysql mysql -umyuser -p

\# enter: mypass



step 5- 

Connect from the host (if you have a MySQL client installed)

\# root

mysql -h 127.0.0.1 -P 3300 -u root -p

\# non-root

mysql -h 127.0.0.1 -P 3300 -u myuser -p





Quick connectivity test from Windows PowerShell (if you want to verify TCP)

Test-NetConnection -ComputerName 127.0.0.1 -Port 3300



Basic SQL checks after connecting

SHOW DATABASES;

USE mydb;

SHOW TABLES;

CREATE TABLE test(id INT AUTO\_INCREMENT PRIMARY KEY, name VARCHAR(100));

INSERT INTO test(name) VALUES('hello');

SELECT \* FROM test;





Optional: run phpMyAdmin to manage the DB via browser

docker run --rm --name phpmyadmin -d -e PMA\_HOST=host.docker.internal -e PMA\_PORT=3300 -p 8080:80 phpmyadmin/phpmyadmin

\# Then open http://localhost:8080 and login with root/rootpass or myuser/mypass



