FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y chromium-browser python3 python3-pip sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install selenium webdriver-manager

COPY main.py /

CMD ["python3", "/main.py"]
