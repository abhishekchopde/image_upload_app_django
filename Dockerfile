FROM ubuntu:16.04


RUN apt-get update && \
        apt-get install -y software-properties-common

RUN apt-get install -y wget

WORKDIR /opt/services/my_app

RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda.sh && \
        /bin/bash Miniconda.sh -b -p /opt/services/my_app/conda && \
        rm Miniconda.sh

ENV PATH /opt/services/my_app/conda/bin:$PATH

RUN mkdir -p media_root/logs/image_upload && touch media_root/logs/image_upload/main_debug.log
RUN mkdir -p media_root/image_upload

RUN mkdir image_upload

ADD . /opt/services/my_app/image_upload

RUN ls

WORKDIR /opt/services/my_app/image_upload
RUN conda env create -f env.yml

ENV PATH=/opt/services/my_app/conda/envs/image_upload/bin:$PATH

RUN pip uninstall --yes bson pymongo
RUN pip install pymongo

EXPOSE 27017 9049

ENV ENV_MEDIA_ROOT="/opt/services/my_app/media_root"
ENV LOGS_ROOT="/opt/services/my_app/media_root/logs"
ARG host='127.0.0.1'

ENV MONGODB_TEST_HOST=${host}
ENV MONGODB_TEST_PORT=27017

CMD python manage.py runserver 0.0.0.0:9049
