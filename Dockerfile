FROM ubuntu:18.04
RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa==1.5.3
WORKDIR /app
ADD . /app
RUN chmod +x ./start_services.sh
CMD ./start_services.sh
