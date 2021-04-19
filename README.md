# S3fileshare
Python util to upload a file to a named S3 bucket, and retrieve an expiring URL for resulting S3 object

$ ./S3fileshare.py --help
usage: S3fileshare.py [-h] -b BUCKET [-o OBJECT] -f FILE [-r REGION] -e EXPIRY

Upload file to S3

optional arguments:
  -h, --help            show this help message and exit
  -b BUCKET, --bucket BUCKET
                        S3 bucket name
  -o OBJECT, --object OBJECT
                        S3 object name
  -f FILE, --file FILE  File name
  -r REGION, --region REGION
                        Region
  -e EXPIRY, --expiry EXPIRY
                        Expiry in seconds
$
