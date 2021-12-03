.PHONY : install shell run image lint test

all : install image test image

install:
	poetry lock
	poetry install

shell:
	poetry shell

run:
	poetry run uvicorn app.main:app --reload --host localhost --port 8000

image:
	docker build --tag adeline --file docker/Dockerfile . 

lint:
	docker build --tag adeline --file docker/Dockerfile . --target lint
	
test:
	docker build --tag adeline --file docker/Dockerfile . --target test
