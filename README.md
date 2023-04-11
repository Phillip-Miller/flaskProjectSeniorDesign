# flaskProjectSeniorDesign

## Deploying on azure

https://learn.microsoft.com/en-us/azure/app-service/tutorial-python-postgresql-app?toc=%2Fazure%2Fdeveloper%2Fpython%2Ftoc.json&bc=%2Fazure%2Fdeveloper%2Fbreadcrumb%2Ftoc.json&tabs=flask%2Cwindows&pivots=deploy-portal

## Installation:

pc ```conda env create -f flaskENV.yml```

mac ```conda env create -f macENV.yml```

activate environment

## Environment Variables:

API_KEY_DICT= {"putTheKeyHere": {"uid": 100}} ->  put inside a .env file if desired in the outer level to fill ENVs

## Run

Run local host from flaskProjectSeniorDesign Directory:

```flask --app geocache run```

Run tests (and ignore 3rd party depreciation warnings):

```pytest tests -W ignore::DeprecationWarning```

## Use

To view our rest api documentation:

``` http://127.0.0.1:8000/api/ui/ ```
