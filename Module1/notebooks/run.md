#### to run with jupyter notebook

uv sync
uv run python -m ipykernel install --user --name module1-uv --display-name "Python (Module1 • uv)"
uv run jupyter notebook notebooks\module1_agent_loop.ipynb