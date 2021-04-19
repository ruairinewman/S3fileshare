# S3fileshare
Python util to upload a file to a named S3 bucket, and retrieve an expiring URL for resulting S3 object

usage: S3fileshare.py [-h] -b BUCKET [-o OBJECT] -f FILE [-r REGION] -e EXPIRY [-s]

Upload file to S3

optional arguments:
  -h, --help            _show this help message and exit_

  -b BUCKET, --bucket BUCKET
                        _S3 bucket name_

  -o OBJECT, --object OBJECT
                        _S3 object name_

  -f FILE, --file FILE  _File name_

  -r REGION, --region REGION
                        _Region_

  -e EXPIRY, --expiry EXPIRY
                        _Expiry in seconds_

  -s, --short           _Require shortened URL_

