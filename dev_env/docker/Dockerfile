FROM python:3.9

RUN mkdir /app

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 80

COPY ./ /app

CMD ["uvicorn", "app:create_app", "--host", "0.0.0.0", "--port", "80", "--reload"]


