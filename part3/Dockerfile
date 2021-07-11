#
# Build stage
#
FROM maven:3.6.0-jdk-11-slim AS build
COPY Checkout/src /home/app/src
COPY Checkout/pom.xml /home/app
RUN curl -L https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/download/v1.3.1/opentelemetry-javaagent-all.jar -o /home/app/opentelemetry-javaagent-all.jar
RUN mvn -f /home/app/pom.xml clean package

#
# Package stage
#
FROM openjdk:11-jre-slim
COPY --from=build /home/app/target/Checkout-0.0.1-SNAPSHOT.jar /usr/local/lib/Checkout.jar
COPY --from=build /home/app/opentelemetry-javaagent-all.jar /usr/local/lib/
EXPOSE 8080
ENTRYPOINT ["java", \
     "-javaagent:/usr/local/lib/opentelemetry-javaagent-all.jar", \
     "-Dserver.host=0.0.0.0", \
     "-Dserver.port=8083", \
     "-Dspring.redis.host=redis", \
     "-Dotel.resource.attributes=service.name=checkout", \
     "-Dotel.metrics.exporter=none", \
     "-jar", "/usr/local/lib/Checkout.jar" \
]
