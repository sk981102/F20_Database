# 실험 용 데이터셋 
출처: kaggle

#### .csv 파일
bestsellers_with_categories.csv : 원본 데이터 셋 

fiction_correct.csv : 픽션 데이터 타입, 무결점 데이터 셋

non-fiction_correct.csv : 픽션 데이터 타입, 무결점 데이터 셋

fiction_incorrect.csv : 픽션 데이터 타입, 결점이 있 데이터 셋

non-fiction_incorrect.csv : 픽션 데이터 타입, 결점이 있는 데이터 셋

결점은 다음과 같음:
1. out-of-bound value 존재
2. NULL Value 존재 
3. data type 틀림 ( ex) int 대신 string )


#### Fiction Schema
```
CREATE TABLE FICTION(
    BOOK_ID INT NOT NULL AUTO_INCREMENT,
    BOOK_NAME VARCHAR(100) NOT NULL,
    AUTHOR VARCHAR(100) NOT NULL,
    RATING FLOAT NOT NULL,
    REVIEWS INT NOT NULL,
    PRICE FLOAT NOT NULL,
    YEAR DATE NOT NULL,
    GENRE VARCHAR(10) NOT NULL,
    CHECK (RATING>=0 & RATING <=5),
    PRIMARY KEY(BOOK_ID), UNIQUE (BOOK_NAME)
)
``` 

#### Non-Fiction Schema
```
CREATE TABLE FICTION(
    BOOK_ID INT NOT NULL AUTO_INCREMENT,
    BOOK_NAME VARCHAR(100) NOT NULL,
    AUTHOR VARCHAR(100) NOT NULL,
    RATING FLOAT NOT NULL,
    REVIEWS INT NOT NULL,
    PRICE FLOAT NOT NULL,
    YEAR DATE NOT NULL,
    GENRE VARCHAR(10) NOT NULL,
    CHECK (RATING>=0 & RATING <=5),
    PRIMARY KEY(BOOK_ID), UNIQUE (BOOK_NAME)
)
``` 
