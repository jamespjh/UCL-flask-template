# syntax=docker/dockerfile:1

FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install -e .

RUN echo hello

CMD ["flask", "--app", "flaskexample", \
     "run",\
     "-h","0.0.0.0", \
     "-p","3000"]