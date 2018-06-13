#!/usr/bin/env python3
#
# Introduction to Cloudwatch logging

import logging
import time

import boto3

logging.getLogger('botocore').setLevel(logging.WARNING)

def main():
    logging.basicConfig(level=logging.INFO)
    client = boto3.client('logs')
    log_group_name =  'aws-utilities'
    log_stream_name = 'test'

    logging.info(f'Creating log group {log_group_name}')
    client.create_log_group(logGroupName=log_group_name)
    logging.info(f'Creating log stream {log_stream_name}')
    client.create_log_stream(
        logGroupName=log_group_name,
        logStreamName=log_stream_name)


    sequence_token = None
    for i in range(100):
        logging.info(f'Putting message {i} to stream')
        body = {
            'timestamp': int(time.time() * 1000),
            'message': f'This is message {i}'
        }

        if i != 0:
            resp = client.put_log_events(
                logGroupName = log_group_name,
                logStreamName = log_stream_name,
                logEvents=[body],
                sequenceToken=sequence_token)
        else:
            resp = client.put_log_events(
                logGroupName = log_group_name,
                logStreamName = log_stream_name,
                logEvents=[body])

        sequence_token = resp['nextSequenceToken']
        time.sleep(1)

if __name__ == '__main__':
    main()
