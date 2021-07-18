#!/usr/bin/env python3
# grocery_store_client.py
import os
import requests
import time
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter


exporter = ConsoleSpanExporter()
resource = Resource.create({"service.name": "shopper"})
provider = TracerProvider(resource=resource)
span_processor = BatchSpanProcessor(exporter)
provider.add_span_processor(span_processor)
provider.add_span_processor(BatchSpanProcessor(JaegerExporter()))
trace.set_tracer_provider(provider)

RequestsInstrumentor().instrument()


def main():
    url = os.getenv("STORE_URL", "http://localhost:5000")
    with trace.get_tracer(__name__).start_as_current_span("going to the grocery store"):
        res = requests.get(url)
        print(res.text)
        res = requests.get("{}/whats-in-store".format(url))
        print(res.text)
        res = requests.get("{}/checkout".format(url))
        print(res.text)


if __name__ == "__main__":
    while 1:
        time.sleep(1)
        main()