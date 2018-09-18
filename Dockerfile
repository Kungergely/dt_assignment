FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python python-pip
RUN pip install pyowm

ADD getweather.py /home/getweather.py

WORKDIR /home

RUN chmod +x getweather.py

ENTRYPOINT ["/usr/bin/python", "getweather.py"]