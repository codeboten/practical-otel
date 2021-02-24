#!/usr/bin/env python3
# grocery_store_client.py
import requests
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.jaeger import JaegerSpanExporter


exporter = ConsoleSpanExporter()
resource = Resource.create({"service.name": "shopper"})
provider = TracerProvider(resource=resource)
span_processor = BatchExportSpanProcessor(exporter)
provider.add_span_processor(span_processor)
provider.add_span_processor(BatchExportSpanProcessor(JaegerSpanExporter("shopper")))
trace.set_tracer_provider(provider)

RequestsInstrumentor().instrument()
with trace.get_tracer(__name__).start_as_current_span("going to the grocery store"):
    res = requests.get("http://localhost:5000")
    print(res.text)