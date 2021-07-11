#
# Build stage
#
FROM golang:1.16
WORKDIR /go/src/github.com/codeboten/practical-otel/part2
COPY go.* .
COPY inventory.go .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o inventory .

#
# Package stage
#
FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=0 /go/src/github.com/codeboten/practical-otel/part2/inventory .
CMD ["./inventory"]