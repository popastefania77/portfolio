FROM python:3.8-alpine

ENV FLASK_APP aplicatie_flask
#ENV FLASK_CONFIG = docker

#3.8 booster
#RUN useradd -rm -d /home/site -s /bin/bash -g root -G sudo -u 1001 site

#3.8 alpine
RUN adduser -D student

USER student

WORKDIR /home/aplicatie_flask/

COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY aplicatie_flask.py aplicatie_flask.py
COPY baza_date.txt baza_date.txt

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r quickrequirements.txt

#WORKDIR /home/sysinfo/app

# runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
#CMD flask run --host 0.0.0.0 -p 5010
