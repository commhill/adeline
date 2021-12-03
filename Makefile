.PHONY : install shell run docker all

install:
	poetry lock
	poetry install

shell:
	poetry shell

run:
	poetry run uvicorn app.main:app --reload --host localhost --port 8000

docker:
	docker build --tag adeline --file docker/Dockerfile . 

all: install docker
