#!/usr/bin/env python3

import logging
import boto3
from boto3.s3.transfer import TransferConfig
from botocore.exceptions import ClientError
from botocore.client import Config
import argparse
import magic, os, sys
from pprint import pprint
import pyshorteners
import requests
import binascii
import string, random

# Logging configuration
logname = 's3upload.log'
logdir = '/logs/'
logfile = os.environ["HOME"] + logdir + logname
logging.basicConfig(filename=logfile, encoding='utf-8', level=logging.WARN)

# Argument parsing
parser = argparse.ArgumentParser(description="Upload file to S3")
parser.add_argument("-b", "--bucket", help = "S3 bucket name", required=False, type=str)
parser.add_argument("-o", "--object", help = "S3 object name", required=False, type=str)
parser.add_argument("-f", "--file", help = "File name", required=True, type=str)
parser.add_argument("-r", "--region", help = "Region", required=False, default=None, type=str)
parser.add_argument("-e", "--expiry", help = "Expiry in seconds", required=True, default=3600, type=int)
parser.add_argument("-s", "--short", help = "Require shortened URL", action="store_true")
args = parser.parse_args()

FILE = args.file
if args.object is None:
	OBJECT = FILE
else:
	OBJECT = args.object
EXPIRY = args.expiry

s3_client = boto3.client('s3')

if(args.bucket) is not None:
	region = s3_client.get_bucket_location(Bucket=args.bucket)['LocationConstraint']
else:
	try:
		region = os.environ['AWS_REGION']
	except:
		try:
			region = args.region
		except:
			print("Can't identify correct region for bucket. Specify AWS region with '-r' switch.")
			sys.exit(1)

if args.bucket is None:
	S3_BUCKET = ''.join(random.choice(string.ascii_lowercase) for i in range(15))
	try:
		s3_client.create_bucket(Bucket=S3_BUCKET)
	except ClientError as e:
		logging.error(e)
		pprint(e)
		sys.exit(1)
else:
	S3_BUCKET = args.bucket

s3_client = boto3.client('s3', config=Config(signature_version='s3v4', region_name=region))

def uploadFileS3(FILE, S3_BUCKET, OBJECT, EXPIRY):
	config = TransferConfig(multipart_threshold=1024*10, max_concurrency=10,
	                    multipart_chunksize=1024*10, use_threads=True)
	filename = FILE
	bucket = S3_BUCKET
	key = OBJECT
	expiration = EXPIRY

	mime = magic.Magic(mime=True)
	contenttype = mime.from_file(filename)

	try:
		s3_client.upload_file(filename, bucket, key, ExtraArgs={ 'ACL': 'private', 'ContentType': contenttype}, Config = config)
	except ClientError as e:
		logging.error(e)
		pprint(e)
		sys.exit(1)

	# File uploaded, presumably. Let's generate the download link
	try:
		response = s3_client.generate_presigned_url('get_object',
			Params={'Bucket': bucket,
			'Key': key},
			ExpiresIn=expiration)
	except ClientError as e:
		logging.error(e)
		return None

  # The response contains the presigned URL
	return response

url = uploadFileS3(FILE, S3_BUCKET, OBJECT, EXPIRY)
if args.short:
	s = pyshorteners.Shortener()
	if url is not None:
		print(s.qpsru.short(url))
else:
	print(url)
