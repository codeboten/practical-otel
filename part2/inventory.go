// inventory.go
package main

import (
	"log"

	"github.com/gin-gonic/gin"
	uuid "github.com/hashicorp/go-uuid"

	"go.opentelemetry.io/contrib/instrumentation/github.com/gin-gonic/gin/otelgin"
	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/exporters/trace/jaeger"
	"go.opentelemetry.io/otel/propagation"
)

func initTracer() {
	otel.SetTextMapPropagator(propagation.TraceContext{})

	_, err := jaeger.InstallNewPipeline(
		jaeger.WithAgentEndpoint("localhost:6831"),
		jaeger.WithProcess(jaeger.Process{ServiceName: "inventory"}),
	)
	if err != nil {
		log.Fatal(err)
	}
}

type Product struct {
	Name  string  `json:"name"`
	Price float64 `json:"price"`
	ID    string  `json:"id"`
}

type Inventory struct {
	Products []Product `json:"products"`
}

func genUUIDv4() string {
	id, _ := uuid.GenerateUUID()
	return id
}

func getInventory() Inventory {
	return Inventory{
		Products: []Product{
			{Name: "potato", Price: 0.99, ID: "1"},
			{Name: "apple", Price: 0.50, ID: "2"},
			{Name: "mango", Price: 1.50, ID: "3"},
		},
	}
}

func main() {
	initTracer()

	r := gin.Default()
	r.Use(otelgin.Middleware("inventory-server"))

	r.GET("/inventory", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"inventory": getInventory(),
		})
	})
	r.Run()
}
