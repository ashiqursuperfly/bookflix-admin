export DEBUG=1
export DJANGO_APP_SECRET_KEY=djangoinsecurev9!w35octvnl6tj6ygjw67difupsapmw5c66n6t4
export DJANGO_ADMIN_USER_NAME=admin
export DJANGO_ADMIN_USER_PASSWORD=admin
export AWS_ACCESS_KEY_ID=AKIAYI2W7LU2SRTKB7LP
export AWS_SECRET_ACCESS_KEY=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
export AWS_S3_REGION_NAME=ap-southeast-1
export AWS_STORAGE_BUCKET_NAME=bookflix-dev
export AWS_RDS_POSTGRES_HOST_URL=ec2-108-128-104-50.eu-west-1.compute.amazonaws.com
export AWS_RDS_POSTGRES_DB_NAME=d3un8idklth2st
export AWS_RDS_POSTGRES_MASTER_USERNAME=ialaswvfefrybt
export AWS_RDS_POSTGRES_MASTER_PASSWORD=b14c856be75c07c3a94d32ac81a7aa7825db013c62d582e5694eb2b1d46b2f21
export ALLOWED_HOSTS=127.0.0.1,localhost

python src/manage.py migrate
python src/manage.py collectstatic
# python src/manage.py createsuperuser
# python src/manage.py inspectdb > inspectdb.py
python src/manage.py runserver