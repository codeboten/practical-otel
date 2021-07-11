module github.com/codeboten/practical-otel

go 1.15

require (
	github.com/gin-gonic/gin v1.7.2
	github.com/hashicorp/go-uuid v1.0.2
	go.opentelemetry.io/contrib/instrumentation/github.com/gin-gonic/gin/otelgin v0.21.0
	go.opentelemetry.io/otel v1.0.0-RC1
	go.opentelemetry.io/otel/exporters/trace/jaeger v1.0.0-RC1
	go.opentelemetry.io/otel/sdk v1.0.0-RC1
)
