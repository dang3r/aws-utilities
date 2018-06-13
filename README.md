# AWS Utility Scripts

A set of utility scripts for miscellaneous tasks on AWS.

# Configuration

Configure AWS credentials via a credentials file, or environment variables. See
[here](http://boto3.readthedocs.io/en/latest/guide/configuration.html) for more
details.

## Instance Types

Aggregate all of your instances by type.

```shell
$make instance_types
c4.large:
- foo
...
c4.xlarge:
- bar
...
c4.2xlarge:
- baz
...
m3.medium:
- dog
r3.medium:
- cat
...
```

## Cloudwatch Logs

Introduction to logging with Cloudwatch. Consisting of:

- log group
- log stream
- events on the stream.

```shell
$ make cloudwatch_logs
INFO:root:Creating log group aws-utilities
INFO:root:Creating log stream test
INFO:root:Putting message 0 to stream
INFO:root:Putting message 1 to stream
INFO:root:Putting message 2 to stream
INFO:root:Putting message 3 to stream
INFO:root:Putting message 4 to stream
INFO:root:Putting message 5 to stream
INFO:root:Putting message 6 to stream
INFO:root:Putting message 7 to stream
...
```
