#!/usr/bin/env python3
#
# Output a yaml file aggregating instances by type

from collections import defaultdict
import yaml

import boto3

RUNNING_INSTANCES_FILTER = [{'Name': 'instance-state-name', 'Values': ['running']}]

def instance_name(instance):
    for tag in instance.tags:
        if tag['Key'] == 'Name':
            return tag['Value']
    return 'No name tag - %s' % (instance.id)

def main():
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.filter(Filters=RUNNING_INSTANCES_FILTER)
    instance_data = defaultdict(list)

    for instance in instances:
        instance_data[instance.instance_type].append(instance_name(instance))
    for d in instance_data.values():
        d.sort()

    print(yaml.dump(dict(instance_data),default_flow_style=False))

if __name__ == '__main__':
    main()
