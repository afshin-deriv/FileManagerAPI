.PHONY: build
build:
	docker build -t myapp .

.PHONY: dev
dev:
	docker run -p 8080:8080 --mount type=bind,source="$(PWD)",target=/app myapp python app.py

.PHONY: prod
prod:
	docker run -p 8080:8080 myapp python app.py
