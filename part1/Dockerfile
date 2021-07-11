FROM python:slim

RUN pip install \
  flask \
  requests

RUN pip install \
  opentelemetry-api \
  opentelemetry-sdk \
  opentelemetry-exporter-jaeger

RUN pip install \
  opentelemetry-instrumentation-flask \
  opentelemetry-instrumentation-requests

WORKDIR /app
ADD grocery_store.py ./
ADD shopper.py ./

CMD ["python", "grocery_store.py"]