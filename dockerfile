FROM python:3.10

WORKDIR ./app

COPY ./requirements.txt /code/

RUN pip install -r /code/requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
