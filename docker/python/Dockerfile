FROM python:3.11

COPY ./t_and_d /srv/www/t_and_d
WORKDIR /srv/www/t_and_d

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN chmod +x ./start.sh
ENTRYPOINT "./start.sh"