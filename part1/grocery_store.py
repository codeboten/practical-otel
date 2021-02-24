#!/usr/bin/env python3
# grocery_store_server.py
from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.exporter.jaeger import JaegerSpanExporter


exporter = ConsoleSpanExporter()
resource = Resource.create({"service.name": "grocery-store"})
provider = TracerProvider(resource=resource)
span_processor = BatchExportSpanProcessor(exporter)
provider.add_span_processor(span_processor)
provider.add_span_processor(
    BatchExportSpanProcessor(JaegerSpanExporter("grocery-store"))
)
trace.set_tracer_provider(provider)


app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)


@app.route("/")
def welcome():
    with trace.get_tracer(__name__).start_as_current_span("welcome message"):
        return "Welcome to the grocery store!"


if __name__ == "__main__":
    app.run()