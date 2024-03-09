FROM python:3.11.6-alpine

WORKDIR /app

COPY . .

RUN pip install pipenv
RUN pipenv sync

ADD Pipfile Pipfile.lock ./

# INSTALL FROM Pipefile.lock FILE
RUN pipenv install --system

ADD . .
