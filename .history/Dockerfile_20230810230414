FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./TokenBalanceTracker /app
COPY ./TokenBalanceTracker/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt
