export DEBUG=1
export DJANGO_APP_SECRET_KEY="django-insecure-v9!w35octv(nl6tj6^ygj&%^w67d*ifupsap$mw5c6*6n6t^)4"
export DJANGO_ADMIN_USER_NAME=admin
export DJANGO_ADMIN_USER_PASSWORD=admin
export AWS_ACCESS_KEY_ID=AKIAYI2W7LU2SRTKB7LP
export AWS_SECRET_ACCESS_KEY=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
export AWS_S3_REGION_NAME=ap-southeast-1
export AWS_STORAGE_BUCKET_NAME=bookflix-dev
export AWS_RDS_POSTGRES_HOST_URL=db-bookflix.ci9z0cyxzrco.ap-southeast-1.rds.amazonaws.com
export AWS_RDS_POSTGRES_DB_NAME=db-bookflix
export AWS_RDS_POSTGRES_MASTER_USERNAME=postgres
export AWS_RDS_POSTGRES_MASTER_PASSWORD=103106115
export ALLOWED_HOSTS="127.0.0.1,localhost"

python src/manage.py migrate
python src/manage.py collectstatic
python src/manage.py runserver