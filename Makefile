.PHONY: help docker-build docker-run docker-logs docker-down

help:
	@echo "Available commands:"
	@echo "	 make docker-build   - Build the Docker image"
	@echo "  make docker-run     - Run the Docker container"
	@echo "  make docker-logs    - View logs of the Docker container"
	@echo "  make docker-down    - Stop and remove the Docker container"

docker-build:
	@echo "Building docker images..."
	docker compose build
	@echo "Docker images built successfully"

docker-run: docker-build
	@echo "Initializing containers..."
	docker compose up -d
	@echo "Containers are running"

docker-logs: docker-run
	docker compose logs -f app

docker-down:
	docker compose down -	v
	@echo "Containers stopped and removed sucessfully"