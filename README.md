# Install UV
- curl -LsSf https://astral.sh/uv/install.sh | sh
- uv  init
- uv venv 
- .venv\Scripts\activate   # or Windows equivalent
- uv pip install -r requirements.txt or  uv sync
- uv pip list

# Run the App
- Change Directory to src
- uv run  main.py


# Exception
-  [remote rejected] main -> main (push declined due to repository rule violations)
   -  How has been added
   -  create base repro