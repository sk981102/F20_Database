# F20_Database
Yonsei F20 Database project. Awarded 1st place and received scholarship for this project.

#### Introduction

This project is to create a data crowsourcing platform. The admin can create tasks to collect data by specifying schema and data type. The submitter can submit the csv file that matches to the schema given certain period of time. The rater can rate the quality of the submitted data and score submitter as well as the dataset.  

#### 실행방법 (How to Run)
1. python 3.8 확인 후 requirements.txt 실행
```
#python version check
python -v

# download requirements.txt
pip install -r requirements.txt 

``` 
2. MariaDB로 Yonsei 라는 이름의 DB 생성
```
#mariaDB 가동
mysql -u root 

#혹은,
sudo mysql -u root

#create Yonsei DB
CREATE DATABASE Yonsei;
``` 
3. myusername, mypassword 의 user 를 생성
```
#User 생성 + 권한 부여
> CREATE USER myusername@localhost IDENTIFIED BY mypassword; 
> GRANT ALL PRIVILEGES ON Yonsei.* TO myusername@localhost;
> FLUSH PRIVILEGES;
``` 
4. migrate 후 서버 실행
``` 
python manage.py migrate
python manage.py runserver
``` 

models.py의 정보를 변경할 경우
``` 
python migrate.py makemigrations
``` 
