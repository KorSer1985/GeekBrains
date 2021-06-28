/* Задача 1
Установите СУБД MySQL. Создайте в домашней директории файл .my.cnf, задав в нем логин и пароль, который указывался при установке.
*/
sudo apt update && sudo apt upgrade
sudo apt install mysql-server
cd
nano .my.cnf
	[mysql]
	user=root
	password=gbmysql8
ctrl+o
ctrl+x

/* Задача 2
Создайте базу данных example, разместите в ней таблицу users, состоящую из двух столбцов, числового id и строкового name.
*/
mysql
CREATE DATABASE IF NOT EXISTS example;
USE example
CREATE TABLE users (
id INT NOT NULL AUTO_INCREMENT,
name CHAR(30) NOT NULL
);


/* Задача 3
Создайте дамп базы данных example из предыдущего задания, разверните содержимое дампа в новую базу данных sample.
*/
mysqldump example > example.sql
mysql
CREATE DATABASE IF NOT EXISTS sample;
exit
mysql sample < example.sql

/* Задача 4
(по желанию) Ознакомьтесь более подробно с документацией утилиты mysqldump. Создайте дамп единственной таблицы help_keyword базы данных mysql. Причем добейтесь того, чтобы дамп содержал только первые 100 строк таблицы.
*/
mysqldump -u root -p --where="true limit 100" mysql help_keyword > help_keyword.sql
