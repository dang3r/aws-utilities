# AWS Utility Scripts

A set of utility scripts for miscellaneous tasks on AWS.

# Configuration

Configure AWS credentials via a credentials file, or environment variables. See
[here](http://boto3.readthedocs.io/en/latest/guide/configuration.html) for more
details.

## Instance Types

Aggregate all of your instances by type.

```shell
make instance_types
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
- foo
r3.medium:
- bar
...
```
