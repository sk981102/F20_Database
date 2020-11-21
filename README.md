# F20_Database
연세대학교 2020년 가을학기 Database 조별과제

#### 실행방법
1. python 3.8 확인 후 requirements.txt 다운로드 혹은 venv 실행
```
#python version check
python -v

# download requirements.txt
pip install -r requirements.txt 

#venv 실행
. venv/bin/activate
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
python migrate.py migrate
python migrate.py runserver
``` 

models.py의 정보를 변경할 경우
``` 
python migrate.py makemigrations
``` 
