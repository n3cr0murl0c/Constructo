#DJANGO -> PYTHON -> DOCKER
# pull official base image
FROM python:3.11-slim

# ENV WORKDIR=/usr/src/v3ntrueSite
RUN mkdir /usr/src/constructo
# set work directory
WORKDIR /usr/src/constructo

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

RUN apt update --yes --quiet && apt install --yes --quiet --no-install-recommends \
    apt-utils \
    build-essential \
    #insert libs to install
    postgresql-server-dev-all \
    # gcc \
    python3-dev \
    musl-dev
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy project
COPY . .

