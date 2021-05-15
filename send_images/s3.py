import logging
import boto3
from botocore.exceptions import ClientError
import os

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = 'instagram-bot/'+ file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name, ExtraArgs={'ACL': 'public-read'})
        # print(response)
    except ClientError as e:
        logging.error(e)
        return False
    return True

path = os.path.dirname(os.path.realpath('__file__'))
print(path)
folder = os.path.join(path,'data_collected\stories\cov19help\\')
print(folder)
upload_file(folder+'2573937872949585141_0.jpg','covid-resource-care-dev','instagram-bot/'+'2573937872949585141_0.jpg')