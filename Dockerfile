FROM python:3-alpine

ENV PYTHONUNBUFFERED 1

LABEL maintainer="Hamed Ahmadi<ahmadihamed167@gmail.com>"

COPY ./requirements requirements 
COPY ./src /src 

RUN apk add --update --no-cache postgresql-client
RUN pip install -U pip 
RUN apk add --update --no-cache --virtual .temp_depend \
        gcc libc-dev linux-headers  postgresql-dev
RUN pip install -r /requirements/dev.txt
RUN apk del .temp_depend 
WORKDIR /src 

RUN adduser -D user 
User user
