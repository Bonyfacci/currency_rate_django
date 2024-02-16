## Django-приложение, которое отображает курс валюты по отношению к рублю на заданную дату

### Стек технологий:

 - ![alt text](https://img.shields.io/badge/Python-3.11.5-grey?style=plastic&logo=python&logoColor=white&labelColor=%233776AB)

 - ![alt text](https://img.shields.io/badge/Django-4.2.10-grey?style=plastic&logo=django&logoColor=white&labelColor=%23092E20)

 - ![alt text](https://img.shields.io/badge/PostgreSQL-15.3-grey?style=plastic&logo=postgresql&logoColor=white&labelColor=%234169E1)

 - ![alt text](https://img.shields.io/badge/Celery-5.3.6-grey?style=plastic&logo=celery&logoColor=white&labelColor=37814A)

 - ![alt text](https://img.shields.io/badge/Redis-5.0.1-grey?style=plastic&logo=redis&logoColor=white&labelColor=DC382D)

 - ![alt text](https://img.shields.io/badge/Docker-v4.25.0-grey?style=plastic&logo=docker&logoColor=white&labelColor=2496ED)

### Описание проекта
Разработано Django-приложение, которое отображает курс валюты по отношению к рублю на заданную дату.

При обращении к приложению по адресу http://localhost:8000/rate/?charcode=AUD&date=2024-01-01, оно выводит
результат в виде JSON в формате:
```json
{
    "charcode": "AUD",  
    "date": "2024-02-16",  
    "rate": 57.0627
}
```

Данные по валютам хранятся в базе данных (PostgreSQL) приложения.

Для пополнения этой базы данных написана асинхронная команда (с использованием Celery), которая раз в сутки (в 12:00) обращается к сервису ЦБ за актуальными курсами валют по адресу:
https://www.cbr-xml-daily.ru/daily_json.js



***

### Запуск через консоль

<details>
<summary>Для запуска через консоль необходимо:</summary>

 - Клонировать проект на собственный диск в новом каталоге
   - Создать виртуальное окружение
   - Установить зависимости командой:
```python
    pip install -r requirements.txt
```
 <details>
   <summary>Прописать переменные окружения в файле `.env.sample`</summary>
   
    ```dotenv
    SECRET_KEY='Секретный ключ Django'
    DEBUG='True/False', например: True
    
    POSTGRES_DB_NAME='Название базы данных', например: 'name_of_db' или 'currency_rate'
    POSTGRES_DB_USER='Пользователь базы данных', например: 'db_user' или 'postgres'
    POSTGRES_DB_PASSWORD='Пароль пользователя базы данных', например: 'your_password'
    POSTGRES_DB_HOST='Хост базы данных', например: '127.0.0.1' или 'localhost' или 'db' (для Docker)
    POSTGRES_DB_PORT='Порт базы данных', например: '5432'

    ADMIN_USERNAME=admin
    ADMIN_EMAIL=admin@example.com
    ADMIN_PASSWORD=admin
   
    CELERY_BROKER_URL=redis://redis:6379/0
    CELERY_RESULT_BACKEND=redis://redis:6379/0
    CELERY_TIMEZONE=Europe/Madrid
    ```
 </details>

 <details>
   <summary>Создать базу данных (в данном проекте используется PostgreSQL)</summary>

 ```python
 psql -U postgres
 create database currency_rate;
 \q
 ```
   </details>

 - Применить миграции командой:
   ```python
   python manage.py migrate
   ```

 <details>
   <summary>Для создания тестового пользователя - администратор:</summary>

   - login: admin@example.com
   - password: admin 
   ```python
        python manage.py csu
   ```
 </details>
 
 <details>
 <summary>Для запуска сервера через терминал:</summary>

  - Запустить Redis (в окне терминала под Ubuntu)
     ```linux
           sudo service redis-server start
     ```
  - Запустить celery (в другом окне терминала)
     ```python
         celery -A config worker -l INFO -P eventlet
     ```
  - Запустить tasks (в другом окне терминала)
     ```python
         celery -A config beat -l info -S django
     ```
  - Запустить сервер (в другом окне терминала)
     ```python
         python manage.py runserver
     ```
 </details>

</details>

***

### Запуск через Docker

<details>
<summary>Для запуска через Docker необходимо:</summary>

- Клонировать проект на собственный диск в новом каталоге
-  <details>
   <summary>Прописать переменные окружения в файле `.env.sample`</summary>
   
    ```dotenv
    SECRET_KEY='Секретный ключ Django'
    DEBUG='True/False', например: True
    
    POSTGRES_DB_NAME='Название базы данных', например: 'name_of_db' или 'currency_rate'
    POSTGRES_DB_USER='Пользователь базы данных', например: 'db_user' или 'postgres'
    POSTGRES_DB_PASSWORD='Пароль пользователя базы данных', например: 'your_password'
    POSTGRES_DB_HOST='Хост базы данных', например: '127.0.0.1' или 'localhost' или 'db' (для Docker)
    POSTGRES_DB_PORT='Порт базы данных', например: '5432'
    
    ADMIN_USERNAME=admin
    ADMIN_EMAIL=admin@example.com
    ADMIN_PASSWORD=admin
   
    CELERY_BROKER_URL=redis://redis:6379/0
    CELERY_RESULT_BACKEND=redis://redis:6379/0
    CELERY_TIMEZONE=Europe/Madrid
    ```
 </details>

- Ввести в терминале команду:
    ```python
        docker-compose up --build
    ```
    > Происходит сборка образа контейнера согласно инструкции в файле Dockerfile и последовательный запуск всех контейнеров согласно инструкции в файле docker-compose.yaml

</details>

***

### Для завершения работы необходимо:

 - Нажать комбинацию клавиш `CTRL + C` в окне терминала

***

<details>
<summary><b>Connect with me:</b></summary>
   <p align="left">
       <a href="mailto:platonovpochta@gmail.com"><img src="https://img.shields.io/badge/gmail-%23EA4335.svg?style=plastic&logo=gmail&logoColor=white" alt="Gmail"/></a>
       <a href="https://wa.me/79217853835"><img src="https://img.shields.io/badge/whatsapp-%2325D366.svg?style=plastic&logo=whatsapp&logoColor=white" alt="Whatsapp"/></a>
       <a href="https://t.me/platonov_sm"><img src="https://img.shields.io/badge/telegram-blue?style=plastic&logo=telegram&logoColor=white" alt="Telegram"/></a>
   </p>
</details>
