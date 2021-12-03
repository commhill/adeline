.PHONY : install shell run image lint test

all : install image test image

install:
	poetry lock
	poetry install

shell:
	poetry shell

run-dev:
	poetry run uvicorn app.main:app --reload --host localhost --port 8000

run-docker:
	docker run -d -p 80:8000 commhill/adeline

image:
	docker build --tag commhill/adeline --file docker/Dockerfile . 

lint:
	docker build --tag commhill/adeline --file docker/Dockerfile . --target lint
	
test:
	docker build --tag commhill/adeline --file docker/Dockerfile . --target test
