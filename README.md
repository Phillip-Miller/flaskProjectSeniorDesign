# flaskProjectSeniorDesign

## Installation:

pc ```conda env create -f flaskENV.yml```

mac ```conda env create -f macENV.yml```

activate environment

## Environment Variables:

API_KEY_DICT= {"putTheKeyHere": {"uid": 100}} -> can put inside a .env file if desired in the outer level to populate ENVs

## Run

Run local host from flaskProjectSeniorDesign Directory:

```flask --app geocache run```

Run tests (and ignore 3rd party depreciation warnings):

```pytest tests -W ignore::DeprecationWarning```

## Use

To view our rest api documentation:

``` http://127.0.0.1:8000/api/ui/ ```

### ToDO

Implement log in with OAuth2.0 ClientSide -> Will ask for user to login with google etc
https://fusionauth.io/learn/expert-advice/oauth/modern-guide-to-oauth#third-party-login-and-registration

Implement API Key Authentication with -> machine communicates with machine
https://fusionauth.io/learn/expert-advice/oauth/modern-guide-to-oauth#machine-to-machine-authorization