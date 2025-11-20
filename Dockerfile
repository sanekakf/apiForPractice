FROM ubuntu
LABEL authors="sasha"
WORKDIR /app
RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update
RUN apt install -y python3
RUN  apt install -y python3-pip
RUN  apt install -y gunicorn
ADD ./requirements.txt requirements.txt
RUN apt install -y python3-flask
RUN apt install -y python3-flask-restful
RUN apt install -y python3-psycopg

COPY . .
EXPOSE 8080
CMD gunicorn main:app --bind 0.0.0.0:8080

