FROM python:3

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

WORKDIR /app

COPY mascarar_dados.py /app/mascarar_dados.py

CMD ["python", "mascarar_dados.py"]
