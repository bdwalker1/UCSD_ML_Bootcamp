FROM ubuntu:latest
LABEL authors="Bruce Walker"
COPY . /app
WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential python3.12-venv
RUN python3 -m venv /app/python-docker-heroku
ENV PATH="/app/python-docker-heroku:$PATH"
RUN /app/python-docker-heroku/bin/pip3 install -Ur requirements.txt
ENTRYPOINT ["/app/python-docker-heroku/bin/python3"]
CMD ["app.py"]