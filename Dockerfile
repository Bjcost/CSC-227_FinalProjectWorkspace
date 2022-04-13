FROM python:3.10.3-slim

ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip \
  && pip install --upgrade pipenv\
  && pip install --upgrade setuptools \
  && apt-get clean \
  && apt-get update \
  && apt install -y build-essential \
  && pip install --upgrade -r /app/requirements.txt

COPY . /app

EXPOSE 8080

CMD ["python", "app.py", "8080"]

