FROM python:3.8

ADD main.py .

RUN pip install pillow pysftp tkinter

CMD [ "python", "./main.py"]