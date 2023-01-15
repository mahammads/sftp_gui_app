FROM python:3.8

WORKDIR /usr/app/src

COPY sftp_module.py ./
COPY main.py ./
RUN  pip install --upgrade pip
RUN pip install pillow pysftp tk

CMD [ "python", "./main.py"]