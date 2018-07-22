#!/usr/bin/env python3
#
# Extract information about an s3 bucket

import boto3
import os
import sys

def main():
    bucket = boto3.resource('s3').Bucket(os.environ['BUCKET_NAME'])
    print('Extracting metadata about', BUCKET_NAME)
    for obj in bucket.objects.all():
        data = (
            obj.last_modified.strftime('%s'),
            obj.size
        )
        print(','.join([str(i) for i in data]))
    print('Finished!')

if __name__ == '__main__':
    main()
