# Dekutree

## Setup
### Virtual Environment (venv)
```ps1
> python -m venv venv
> .\venv\Scripts\activate
(venv) > python -m pip install -r requirements.txt
```


## Test
```ps1
> python -m pip install -e .
> python -m pip install pytest
> python -m pytest ./test
```