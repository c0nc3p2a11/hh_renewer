FROM mcr.microsoft.com/playwright/python:v1.37.0-jammy

WORKDIR /opt/hh_renewer

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "./main.py"]