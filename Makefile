.PHONY: run test process docker-up docker-down docker-build

run:
	uvicorn app.main:app --reload

test:
	pytest

process:
	python -m scripts.process_transcript

docker-build:
	docker build -t studyvault-api .

docker-up:
	docker compose up --build

docker-down:
	docker compose down
