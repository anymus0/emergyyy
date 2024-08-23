FROM docker.io/library/python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir --use-pep517 -r requirements.txt

COPY . .

CMD [ "python", "./src/main.py" ]
