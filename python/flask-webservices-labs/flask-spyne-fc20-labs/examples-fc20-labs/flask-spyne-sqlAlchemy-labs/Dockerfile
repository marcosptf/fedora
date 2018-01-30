FROM python:2.7.14

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./main.py"]

