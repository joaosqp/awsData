FROM python:3

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

WORKDIR /app

COPY carguru.py /app/carguru.py

CMD ["python", "carguru.py"]
