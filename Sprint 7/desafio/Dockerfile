FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install boto3

CMD [ "python", "s3_ingestao.py" ]

# Comandos docker

# docker build -t s3_ingestao.py . 

# docker run -v /app s3_ingestao.py