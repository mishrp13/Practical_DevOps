import boto3

def lambda_handler(event,context):
    ec2=boto3.client('ec2')

    response= ec2.describe_snapshots(OwnerIds=['self'])

    instance_response= ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'values': ['running']}])
    active_instance_ids=set()


    for reservation in instance_response['Reservations']:
        for instance in reservation['instances']:
            active_instance_ids.add(instance['InstanceId'])

    
    for snapshot in response['snapshots']:
        snapshot_id=snapshot['snapshotId']
        volume_id=snapshot.get('volumeId')

        if not volume_id:
            ec2.delete_snapshot(SnapsShotId=snapshot_id)
            print(f"Delete EBS snapshot {snapshot_id} as it was not attached to any volume")

        else:

            try:
                volume_response= ec2.describe_volumes(VolumeIds=[volume_id])
                if not volume_response['volumes'][0]['Attachments']:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any instances: ")
            except ec2.exceptions.ClientError as e:
                if e.response['ERROR']['code'] == "InvalidVolume.NotFound":
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as its associated volume not found")
