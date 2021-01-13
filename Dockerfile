FROM python:3.7

COPY ./requirements.txt requirements.txt
RUN pip install -r ./requirements.txt

COPY . code
WORKDIR code

RUN chmod 777 vars.sh

EXPOSE 8000



