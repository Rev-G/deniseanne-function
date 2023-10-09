# deniseanne-function

deniseanne.com google cloud function

## API's to enable

Need to enable the following api's

- Cloud Functions
- Cloud Build
- Artifact Registry
- Cloud Run
- Logging
- Secret Manager

## setup

`python3 -m venv env`

`source env/bin/activate`

`python3 -m pip install --upgrade pip`

`python3 -m pip install -r requirements.txt`

or

`python3 -m pip install functions-framework`

## deploy

create a new deployment service account and create a key with the following roles

- Cloud Functions Developer


`/Users/gary/mycode/google-cloud-sdk/bin/gcloud init`

should change the "python-http-function" to a different name

```bash
/Users/gary/mycode/google-cloud-sdk/bin/gcloud functions deploy python-http-function \
--gen2 \
--runtime=python311 \
--region=us-east1 \
--source=. \
--entry-point=da_cart \
--trigger-http \
--allow-unauthenticated
```

Using cloud build??

<!-- gcloud builds submit --region=us-east1 --config CONFIG_FILE_PATH SOURCE_DIRECTORY -->
`cd /Users/gary/mycode/Rev-G/deniseanne-function/function`
`gcloud builds submit --region=us-east1 --config cloudbuild.yml .`

## remove

`/Users/gary/mycode/google-cloud-sdk/bin/gcloud functions delete python-http-function --gen2 --region us-east1`

## local test

`functions-framework --target da_cart --debug`

## logout 

`gcloud auth revoke --all`

https://cloud.google.com/functions/docs/create-deploy-gcloud#functions_quickstart_helloworld-python

https://cloud.google.com/functions/docs/samples/functions-helloworld-http#functions_helloworld_http-python

https://pypi.org/project/functions-framework/

https://support.thrivecart.com/help/using-webhook-notifications/

https://webhook.site/

Need this!!!
https://cloud.google.com/functions/docs/configuring/env-var
better yet this!!!
https://cloud.google.com/functions/docs/configuring/secrets