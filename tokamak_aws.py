import configparser
import boto3
import paramiko
import time
import json

config = configparser.ConfigParser()
config.read('config.ini')

## variables

### env:aws IAM and region
aws_access_key_id = config['AWS']['AWS_ACCESS_KEY']
aws_secret_access_key = config['AWS']['AWS_SECRET_KEY']

### env:instance
basic_image_id = config['INSTANCE']['BASIC_IMAGE_ID']
rootchain_image_id = config['INSTANCE']['ROOTCHAIN_IMAGE_ID']
operator_image_id = config['INSTANCE']['OPERATOR_INAGE_ID']
user_image_id = config['INSTANCE']['USER_IMAGE_ID']

instance_type = config['INSTANCE']['INSTANCE_TYPE']
security_group_id = config['INSTANCE']['SECURITY_GROUP_ID']
key_name = config['INSTANCE']['KEY_NAME']

region_name = config['INSTANCE']['REGION_NAME']

### env:paramiko
ssh_username = config['SSH']['SSH_USERNAME']
ssh_pemfile = config['SSH']['SSH_PEMFILE']

### network variables
rootchain_ip_address = ""
operator_ip_address = ""
usernode_ip_address = ""

### blockchain variables
genesis_data = ""

## utility functions
def ssh_execute(host="", command=""):
    pk = paramiko.RSAKey.from_private_key_file(ssh_pemfile)
    p_client = paramiko.SSHClient()
    p_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    p_client.connect( hostname = host, username = ssh_username, pkey = pk )
    stdin, stdout, stderr = p_client.exec_command(command, get_pty=True)
    out_list = stdout.readlines()
    return out_list

## setup ec2 client
client = boto3.client(
    'ec2',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

ec2 = boto3.resource(
    'ec2',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

##############################
#### OPERATOR CONTROLLER  ####
##############################

def create_operator_instance(operator_name):
    operator_instance = ec2.create_instances(
        ImageId=operator_image_id,
        InstanceType=instance_type,
        SecurityGroupIds=[security_group_id],
        KeyName=key_name,
        TagSpecifications=[
            {
                'ResourceType':'instance',
                'Tags':[{'Key' : 'Name', 'Value' : operator_name}]
            },
        ],
        MinCount=1,
        MaxCount=1,
    )

    print("op id->>>>>", operator_image_id)

    operator_id = operator_instance[0].id

    return operator_instance[0]

## And make signer.pass
def change_account_operator(op_ip, op_key, op_addrs, op_pass, chain_id, is_pre, epoch, nodekey, rootchain_ip):
    key1 = "<operator key>"
    key2 = "<operator address>"
    key3 = "<password>"
    key4 = "<chain id>"
    key5 = "<pre asset true or false>"
    key6 = "<epoch lenth of plasma>"
    key7 = "<node key hex>"
    key8 = "<rootchain ip address>"

    cmdg = "sed -i "
    cmd1 = "-e 's/" + key1 + "/" + op_key + "/g' "
    cmd2 = "-e 's/" + key2 + "/" + op_addrs + "/g' "
    cmd3 = "-e 's/" + key3 + "/" + op_pass + "/g' "
    cmd4 = "-e 's/" + key4 + "/" + chain_id + "/g' "
    cmd5 = "-e 's/" + key5 + "/" + is_pre + "/g' "
    cmd6 = "-e 's/" + key6 + "/" + epoch + "/g' "
    cmd7 = "-e 's/" + key7 + "/" + nodekey + "/g' "
    cmd8 = "-e 's/" + key8 + "/" + rootchain_ip + "/g' "
    cmd9 = "/home/ubuntu/variables.list"

    cmd = cmdg + cmd1 + cmd2 + cmd3 + cmd4 + cmd5 + cmd6 + cmd7 + cmd8 + cmd9
    cmd2 = " && /home/ubuntu/3_make.signer.pass.sh"
    # print(cmd)
    return ssh_execute(op_ip, cmd+cmd2)

def deploy_rootchain_contract(ip_address):
    return ssh_execute(host=ip_address, command="/home/ubuntu/1_deploy.rootchain.sh")

def export_genesis(ip_address):
    output = ssh_execute(host=ip_address, command="cat /home/ubuntu/genesis.json")
    return json.loads(output[0])

def initialize_operator_blockchain(ip_address):
    output = ssh_execute(host=ip_address, command="/home/ubuntu/2_init.oper.sh")
    return output

def run_operator(ip_address):
    return ssh_execute(host=ip_address, command="/home/ubuntu/4_run.operator.sh")

def restart_operator(ip_address):
    out1 = ssh_execute(host=ip_address, command="/home/ubuntu/init.all.sh")
    out2 = ssh_execute(host=ip_address, command="/home/ubuntu/4_run.operator.sh")
    return [out1, out2]

##############################
#### ROOTCHAIN CONTROLLER ####
##############################

def create_rootchain_instance(rootchain_name):
    ### 1.1 initiate rootchain instance
    rootchain_instance = ec2.create_instances(
        ImageId=rootchain_image_id,
        InstanceType=instance_type,
        SecurityGroupIds=[security_group_id],
        KeyName=key_name,
        TagSpecifications=[
            {
                'ResourceType':'instance',
                'Tags':[{'Key' : 'Name', 'Value' : rootchain_name}]
            },
        ],
        MinCount=1,
        MaxCount=1,
    )

    rootchian_id = rootchain_instance[0].id

    return rootchain_instance[0]

def run_rootchain(ip_address):
    out = ssh_execute(host=ip_address, command="bash /home/ubuntu/run.rootchain.sh")
    return out[1]

def deploy_manager_contract(ip_address):
    out = ssh_execute(host=ip_address, command="bash /home/ubuntu/stake/1_deploy.manager.sh")
    return out

def deploy_powerton_contract(ip_address):
    out = ssh_execute(host=ip_address, command="bash /home/ubuntu/stake/2_deploy.powerton.sh")
    return out

def start_powerton_contract(ip_address):
    out = ssh_execute(host=ip_address, command="bash /home/ubuntu/stake/4_start.powerton.sh")
    return out

def export_manager_command(ip_address):
    out = ssh_execute(host=ip_address, command="bash /home/ubuntu/stake/3_export.manager.sh")
    return out

def export_manager_contract(ip_address):
    a = ssh_execute(host=ip_address, command="cat /home/ubuntu/manager.json")
    b = [i.strip(" ").strip(",\r\n").strip('":').split(" ") for i in a[1:6]]
    c = [k[1:]  for j,k in b]
    d = ['TON', 'WTON', 'DepositManager', 'RootChainRegistry', 'SeigManager']
    return {k:v for k in d for v in c}

def initialize_rootchain(ip_address):
    out = ssh_execute(host=ip_address, command="bash /home/ubuntu/reset.rootchain.sh")
    return out[0]

def change_rootchain_account(ip_address, key0, key1, key2, key3, key4, key5, operator, delay, seigniorage, p_round):
    priv0 = "key1"
    priv1 = "key2"
    priv2 = "key3"
    priv3 = "key4"
    priv4 = "key5"
    priv5 = "key6"

    op = "<operator address>"
    w_delay = "<withdrawal delay>"
    seig = "<seigniorage per block>"
    round = "<round time second>"

    cmdg = "sed -i "
    cmd0 = "-e 's/" + priv0 + "/" + key0 + "/g' "
    cmd1 = "-e 's/" + priv1 + "/" + key1 + "/g' "
    cmd2 = "-e 's/" + priv2 + "/" + key2 + "/g' "
    cmd3 = "-e 's/" + priv3 + "/" + key3 + "/g' "
    cmd4 = "-e 's/" + priv4 + "/" + key4 + "/g' "
    cmd5 = "-e 's/" + priv5 + "/" + key5 + "/g' "
    cmd6 = "-e 's/" + op + "/" + operator + "/g' "
    cmd7 = "-e 's/" + w_delay + "/" + delay + "/g' "
    cmd8 = "-e 's/" + seig + "/" + seigniorage + "/g' "
    cmd9 = "-e 's/" + round + "/" + p_round + "/g' "
    cmd10 = "/home/ubuntu/account.variable"

    cmd = cmdg + cmd0 + cmd1 + cmd2 + cmd3 + cmd4 + cmd5 + cmd6 + cmd7 + cmd8 + cmd9 + cmd10
    ssh_execute(ip_address, cmd)

##############################
#### USERNODE CONTROLLER  ####
##############################

def create_usernode_instance(name):

    usernode_instance = ec2.create_instances(
        ImageId=user_image_id,
        InstanceType='t2.small',
        SecurityGroupIds=[security_group_id],
        KeyName=key_name,
        TagSpecifications=[
            {
                'ResourceType':'instance',
                'Tags':[{'Key' : 'Name', 'Value' : name}]
            },
        ],
        MinCount=1,
        MaxCount=1,
    )

    usernode_id = usernode_instance[0].id

    return usernode_instance[0]

def set_usernode_variable(user_ip, root_ip, operator_ip, enode_value):
    key1 = "<rootchain ip>"
    key2 = "<operator ip>"
    key3 = "<enode value>"

    cmdg = "sed -i "
    cmd0 = "-e 's/" + key1 + "/" + root_ip + "/g' "
    cmd1 = "-e 's/" + key2 + "/" + operator_ip + "/g' "
    cmd2 = "-e 's/" + key3 + "/" + enode_value + "/g' "
    cmd3 = "/home/ubuntu/variables.list"

    cmd = cmdg + cmd0 + cmd1 + cmd2 + cmd3
    return ssh_execute(user_ip, cmd)

def import_genesis_usernode(usernode_ip, genesis):
    gen = json.dumps(genesis)
    output = ssh_execute(host=usernode_ip, command="echo '" + gen + "' | python3 -mjson.tool > /home/ubuntu/genesis.json")
    return output

def check_genesis(user_ip):
    while 1:
        cmd = '! [ -e "/home/ubuntu/genesis.json" ] && echo "file does not exist"'
        output_checkfile = ssh_execute(host=user_ip, command=cmd)
        # print(output_checkfile)
        print("...")
        if not output_checkfile:
            print("genesis.json created!")
            break;
        time.sleep(0.5)
    return

def initialize_usernode(usernode_ip):
    return ssh_execute(host=usernode_ip, command="./1_init.user.sh")

def run_usernode(usernode_ip):
    output36 = ssh_execute(host=usernode_ip, command="./2_run.user.sh")
    return output36

#############################
#### INSTANCE CONTROLLER ####
#### https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html?highlight=create_instances#EC2.ServiceResource.create_instances

def get_instance_ip(instance_id):
    ins_json = client.describe_instances(InstanceIds=[instance_id])
    ip_addrs = ins_json['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['Association']['PublicIp']
    return ip_addrs

def get_instance_resource(instance_id):
    return ec2.Instance(instance_id)

def get_log_tail(ip_address, file):
    out = ssh_execute(host=ip_address, command="tail " + file)
    return out
