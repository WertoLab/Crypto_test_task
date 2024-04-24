FROM python:3.11.4

WORKDIR /transactions_filter_app

COPY ./requirements.txt /transactions_filter_app/

RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY . /transactions_filter_app

EXPOSE 8000

CMD gunicorn main:app --workers=10 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --timeout=600
