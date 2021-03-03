module github.com/codeboten/practical-otel

go 1.15

require (
	github.com/gin-gonic/gin v1.6.3
	github.com/hashicorp/go-uuid v1.0.2 // indirect
	go.opentelemetry.io/contrib/instrumentation/github.com/gin-gonic/gin/otelgin v0.17.0
	go.opentelemetry.io/contrib/instrumentation/github.com/gorilla/mux/otelmux v0.17.0 // indirect
	go.opentelemetry.io/otel v0.17.0
	go.opentelemetry.io/otel/exporters/stdout v0.17.0
	go.opentelemetry.io/otel/exporters/trace/jaeger v0.17.0 // indirect
	go.opentelemetry.io/otel/sdk v0.17.0
)
