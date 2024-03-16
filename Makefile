.PHONY: format
format:
	black -t py39 meggie_difference

.PHONY: check
check:
	black --check -t py39 meggie_difference
	pylama meggie_difference

.PHONY: test
test:
	pytest -s
