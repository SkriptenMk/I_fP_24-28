jboptions = --max-size-webp 20MB
build: docs/_build
docs/_build: .venv/bin/jupyter-book docs/_static/MathJax/MathJax.js
	(cd docs/; ../.venv/bin/jupyter-book build $(jboptions) --html)
	touch docs/_build/html/.nojekyll
rebuild: .venv/bin/jupyter-book docs/_static/MathJax/MathJax.js
	(cd docs/; ../.venv/bin/jupyter-book build $(jboptions) --html)
	touch docs/_build/html/.nojekyll
start: .venv/bin/jupyter-book docs/_static/MathJax/MathJax.js
	(cd docs/; ../.venv/bin/jupyter-book start $(jboptions))
	touch docs/_build/html/.nojekyll
.venv:
	python3 -m venv .venv
.venv/bin/jupyter-book: .venv
	.venv/bin/pip install -r requirements.txt
clean:
	rm -r .venv docs/_build
.PHONY: clean rebuild start build

## MathJax/MathJax.js
docs/_static/MathJax:
	mkdir -p $@
docs/_static/MathJax/MathJax.js: docs/_static/MathJax
	wget https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js -O  $@
