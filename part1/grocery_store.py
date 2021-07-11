#!/usr/bin/env python3
# grocery_store_server.py
import os

import requests

from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter


exporter = ConsoleSpanExporter()
resource = Resource.create({"service.name": "grocery-store"})
provider = TracerProvider(resource=resource)
span_processor = BatchSpanProcessor(exporter)
provider.add_span_processor(span_processor)
provider.add_span_processor(BatchSpanProcessor(JaegerExporter()))
trace.set_tracer_provider(provider)


app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()


@app.route("/")
def welcome():
    with trace.get_tracer(__name__).start_as_current_span("welcome message"):
        return "Welcome to the grocery store!"


@app.route("/whats-in-store")
def whats_in_store():
    inventory_service = os.environ.get(
        "INVENTORY_SERVICE_URL", "http://localhost:8080/inventory"
    )
    res = requests.get(inventory_service)
    return res.text


@app.route("/checkout")
def checkout():
    checkout_service = os.environ.get(
        "CHECKOUT_SERVICE_URL", "http://localhost:8083/orders"
    )
    order = {
        "items": [
            {"id": "1", "quantity": 10},
            {"id": "2", "quantity": 20},
        ],
    }
    res = requests.post(checkout_service, json=order)
    return res.text


if __name__ == "__main__":
    app.run(host="0.0.0.0")