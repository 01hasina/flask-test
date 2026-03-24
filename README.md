*cloner le repository Github*
git clone https://github.com/01hasina/flask-test.git
cd flask-test

*creer artifact registry*
gcloud artifacts repositories create flask-demo \
  --repository-format=docker \
  --location=us-central1 \
  --description="Flask repo"

*configure docker*
gcloud auth configure-docker us-central1-docker.pkg.dev

*activate apis google*
gcloud services enable artifactregistry.googleapis.com \
  cloudbuild.googleapis.com \
  run.googleapis.com

*build and push image*
gcloud builds submit --tag us-central1-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/flask-demo/flask-app:1.0.0

*deploy on cloud run*
gcloud run deploy flask-app \
  --image us-central1-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/flask-demo/flask-app:1.0.0 \
  --region us-central1 \
  --allow-unauthenticated

*list of the services and click to the url of your flask app*
gcloud run services list

*if you update your website*
push to the repo github
build and push the image
deploy on cloud run