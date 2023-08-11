FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./APP /app
COPY ./APP/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt
