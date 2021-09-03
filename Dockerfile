FROM python:3.7

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

RUN export PYTHONPATH='${PYTHONPATH}:/flask_app'

COPY . .

CMD ["python", "./run.py"]
