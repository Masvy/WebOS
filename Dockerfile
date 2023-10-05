FROM python:3.10-alpine

RUN mkdir /src
RUN mkdir /users
WORKDIR /src

ENV USER_ROOT=/user

ADD ./telegramos .
ADD ./requirements.txt .

RUN pip install -r ./requirements.txt