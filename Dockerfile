FROM python:3.10

WORKDIR /app

RUN apt-get update && \
    apt-get install -y chromium-browser && \
    rm -rf /var/lib/apt/lists/*

RUN pip install selenium webdriver-manager

COPY . /app

CMD ["python", "main.py"]
