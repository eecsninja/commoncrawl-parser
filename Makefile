
# Note: Image name must match docker-compose.yml
SPARK_DOCKER_IMAGE_NAME := qadium/spark-commoncrawl

.PHONY: build
build:
	docker build -t $(SPARK_DOCKER_IMAGE_NAME) .

.PHONY: up
up: 
	docker-compose -f docker-compose.yml up -d

.PHONY: down
down:
	docker-compose -f docker-compose.yml down

.PHONY: spark-shell
spark-shell:
	docker-compose exec master bash

