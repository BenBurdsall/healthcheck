FROM arm32v7/python:3
#FROM python:3.10-rc-alpine3.12



# update apk repo
#RUN echo "http://dl-4.alpinelinux.org/alpine/v3.12/main" >> /etc/apk/repositories && \
#    echo "http://dl-4.alpinelinux.org/alpine/v3.12/community" >> /etc/apk/repositories

RUN apk add --no-cache tzdata
RUN apk --no-cache add curl
ENV TZ Europe/London

WORKDIR /usr/src/app

COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install --upgrade pip setuptools wheel && pip3 install -r requirements.txt
ENV PYTHONUNBUFFERED 1
ENV APPVERSION 1
ENV FLASK_APP=app.py
COPY *.py ./
EXPOSE 5000
ENTRYPOINT [ "flask"]
CMD [ "run", "--host", "0.0.0.0" ]