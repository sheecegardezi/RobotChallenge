FROM ubuntu:latest
MAINTAINER fnndsc "sheecegardezi@gmail.com"

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

WORKDIR /app
COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt \
  && pip3 install -e .

ENTRYPOINT ["python3", "-m", "robotchallenge"]