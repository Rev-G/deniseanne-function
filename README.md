# deniseanne-function

deniseanne.com google cloud function

## setup

`python3 -m venv env`

`source env/bin/activate`

`python3 -m pip install --upgrade pip`

`python3 -m pip install -r requirements.txt`

or

`python3 -m pip install functions-framework`

## deploy

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

## remove

`/Users/gary/mycode/google-cloud-sdk/bin/gcloud functions delete python-http-function --gen2 --region us-east1`

## local test

`functions-framework --target da_cart --debug`

https://cloud.google.com/functions/docs/create-deploy-gcloud#functions_quickstart_helloworld-python

https://cloud.google.com/functions/docs/samples/functions-helloworld-http#functions_helloworld_http-python

https://pypi.org/project/functions-framework/

https://support.thrivecart.com/help/using-webhook-notifications/

https://webhook.site/

Need this!!!
https://cloud.google.com/functions/docs/configuring/env-var
better yet this!!!
https://cloud.google.com/functions/docs/configuring/secrets