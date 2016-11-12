FROM python:2.7

WORKDIR /code
#VOLUME /code

RUN cd /code \
    && virtualenv venv \
    && ./venv/bin/pip install pypicloud[server] uwsgi

ENV ENV prod

ADD make_config.py /code
ADD entry.sh /code

ENTRYPOINT ["bash", "/code/entry.sh"]
