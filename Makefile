build: docs/_build
docs/_build: .venv/bin/jupyter-book
	(cd docs/; ../.venv/bin/jupyter-book build --html)
	touch docs/_build/html/.nojekyll
.venv:
	python3 -m venv .venv
.venv/bin/jupyter-book: .venv
	.venv/bin/pip install -r requirements.txt
clean:
	rm -r .venv docs/_build
.PHONY: clean build
