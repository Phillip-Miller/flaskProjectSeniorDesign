# flaskProjectSeniorDesign

## Installation:

pc ```conda env create -f flaskENV.yml```

mac ```conda env create -f macENV.yml```

activate environment

## Environment Variables:

SECRET_KEY='insertkeyhere' -> can put inside a .env file if desired

Used to seed encryption

## Run

Run local host from flaskProjectSeniorDesign Directory:

```flask --app geocache run```

Run tests (and ignore 3rd party depreciation warnings):

```pytest tests -W ignore::DeprecationWarning```

## Use

To view our rest api documentation:

``` http://127.0.0.1:8000/api/ui/ ```
