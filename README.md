# Securin_Assessment_2_Delhi_Weather

# 

FastAPI is a Python library for dealing with API endpoints and how to either GET or POST data.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install FastAPI.

```bash
pip install fastapi
pip install uvicorn
```

## Usage

```python
from fastapi import FastAPI
app = FastAPI()
@app.get('/necessary_path/')
async def operation(props):
      #necessary function on props passed
```
