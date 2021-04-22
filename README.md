# S3fileshare
Python util to upload a file to a S3 bucket, and retrieve an expiring URL for resulting S3 object

## Features
* Bucket region autodetect
* Random bucket name auto-generated if not specified
* New bucket ACL defaults to 'private'
* Expiry defaults to 3600s/1hr
* Supports outputting short URL

```
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
	
	--acl           _specify canned ACL (defaults to 'private')_

```
