FROM python:3

RUN pip install flask

RUN git clone https://github.com/MrManz/dockerDemoApp.git

CMD ["python", "./dockerDemoApp/app.py"]

EXPOSE 80/tcp