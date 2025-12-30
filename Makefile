.PHONY: help docker-build docker-run docker-stop docker-logs docker-down run

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

docker-stop:
	@echo "Stopping containers..."
	docker compose stop
	@echo "Containers stopped successfully"

docker-down:
	docker compose down -	v
	@echo "Containers stopped and removed sucessfully"

install:
	@echo "Installing dependencies with uv..."
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv sync
	@echo "Dependencies installed successfully"

run: install
	@echo "Running the application..."
	uv run main.py