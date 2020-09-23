import config
import boto3
from botocore.exceptions import NoCredentialsError

SECRET_KEY = config.aws_secret_access_key
ACCESS_KEY = config.aws_access_key_id


def upload_to_aws(local_file, bucket, s3_file, ExtraArgs):
    s3 = boto3.client('s3',region_name="eu-west-2", aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file, ExtraArgs)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


def upload_index():
    upload_to_aws('E:\Dropbox\Dropbox\Dev\Work\dad.boringhell.com\index.html', 'www.dad.boringhell.com', 'index.html', ExtraArgs={'ContentType': 'text/html'})

