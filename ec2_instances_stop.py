import os, json

find_running_ec2_command = "aws ec2 describe-instances --filters Name=instance-state-name,Values=running"
stop_ec2_command = "aws ec2 stop-instances --instance-ids %s"

stream = os.popen(find_running_ec2_command)
json_result = json.loads(stream.read())

instances_json_list = list((map(lambda e: e['Instances'], json_result['Reservations'])))
instances = []
for instance in instances_json_list:
    instances += instance

instances_ids = " ".join(list(map(lambda i: i['InstanceId'], instances)))
if (instances_ids):
    os.system(stop_ec2_command % instances_ids)
    print("All instances is stopped")
else:
    print("No running instances")
