FROM amazonlinux:2.0.20200602.0

RUN yum install -y python3-pip zip && \
    yum clean all

RUN python3.7 -m pip install --upgrade pip


# docker cp 7b4cd:/root/camada_desafio/python ./  -> Comando para copiar arquivo