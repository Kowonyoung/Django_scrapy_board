# ๐ก IT news crawling site ๊ตฌ์ถ

> crawling IT news site by using Scrapy and Django

<br/><br/>

## ๐ Project description

- IT ๋ด์ค ํฌ๋กค๋ง ์น์ฌ์ดํธ ๋ง๋ค๊ธฐ

โ `Scray`๋ฅผ ์ด์ฉํ์ฌ ๋ค์ด๋ฒ IT ๋ด์ค๋ฅผ ํฌ๋กค๋งํ์ฌ model์ ์ฐ๋๋ db์ ์ ์ฅ

โ `django MTV` ํจํด์ ์ด์ฉํ์ฌ ํฌ๋กค๋งํ ๋ฐ์ดํฐ๋ฅผ ๋ณด์ฌ์ฃผ๋ ์น์ฌ์ดํธ ๊ตฌ์ถ

โ ์ต์  ๋ฐ์ดํฐ ๊ฐ์ ธ์ค๊ธฐ `button`์ ํตํ ๋ด์ค ํฌ๋กค๋ง

โ ํค์๋ ์๋ ฅ์ ํตํ `search` ๊ธฐ๋ฅ ์ถ๊ฐ

โ DB์ ์ ์ฅ๋ ๋ฐ์ดํฐ๋ฅผ ์ ๊ณตํ  ์ ์๋ `RESTful API` ์ค๊ณ





---

<br/><br/>

## ๐ป Start Project 

```python
# Scrapy Project
scrapy startproject myscrapy # start scrapy project
scrapy genspider mybot domin # scrapy bot
```

```python
# Django project
django-admin startproject django-scrapy-news # ํ๋ก์ ํธ ์์ฑ 
python manage.py migrate # db ์ ์ฅ
python manage.py startapp news # ๋ด์ค app ์์ฑ
# ๋ชจ๋ธ ์ค๊ณ -> ๋ทฐ ์ค๊ณ -> ํํ๋ฆฟ ์ค๊ณ
```



---

<br/><br/>

## Project structure

![structure](README.assets/structure.png)

<br/>



---

<br/><br/>

## ๐ Project result

> project demo show

<br/>

#### before crawling

![before_crawling](README.assets/before_crawling.png)

<br/>

#### After crawling

![after_crawling](README.assets/after_crawling-1611982752175.png)

<br/>

#### Search engine

![search_engine](README.assets/search_engine.png)

<br/>

#### RESTful API

![restAPI](README.assets/restAPI.png)

---

<br/><br/>

## ๐ป Development Stack

|    division     |       stack        |
| :-------------: | :----------------: |
|    Framework    |       Django       |
|    Front-end    | Python, html, css  |
|    Back-end     |   Python, Scrapy   |
|       db        |       Sqlite       |
| Code Management |    Git, Github     |
|       IDE       | Visual Studio Code |

