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

### for staking command
staking_amount = 0

### config setting
def config_set(parameter):
    global aws_access_key_id, aws_secret_access_key, basic_image_id, instance_type, security_group_id, key_name, region_name, ssh_username, ssh_pemfile
    aws_access_key_id = parameter['ac_key']
    aws_secret_access_key = parameter['sec_key']

    ### env:instance
    basic_image_id = parameter['img_id']

    instance_type = parameter['ins_type']
    security_group_id = parameter['sec_group_id']
    key_name = parameter['key_name']
    region_name = parameter['region_name']

    ### env:paramiko
    ssh_username = parameter['ssh_user']
    ssh_pemfile = parameter['ssh_pem']
    

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

#######################
##### CONTROL PEM #####
#######################

def create_pem(pem_name):
    response = ec2.create_key_pair(KeyName=pem_name)

    key_pair = str(response.key_material)
    key_finger_print = str(response.key_fingerprint)

    return key_pair, key_finger_print

def delete_pem(pem_name):
    response = client.delete_key_pair(KeyName=pem_name)

    return response
    

##############################
###### COMMON INSTANCE  ######
##############################

def create_instance(instance_name):
    created_instance = ec2.create_instances(
        ImageId=basic_image_id,
        InstanceType=instance_type,
        SecurityGroupIds=[security_group_id],
        KeyName=key_name,
        TagSpecifications=[
            {
                'ResourceType':'instance',
                'Tags':[{'Key' : 'Name', 'Value' : instance_name}]
            },
        ],
        MinCount=1,
        MaxCount=1,
    )

    created_instance_id = created_instance[0].id

    return created_instance[0]

##############################
#### OPERATOR CONTROLLER  ####
##############################

## And make signer.pass
def change_account_operator(parameter):
    key1 = "<operator key>"
    key2 = "<operator address>"
    key3 = "<password>"
    key4 = "<deploy gasprice>"
    key5 = "<commit gasprice>"
    key6 = "<stamina amount>"
    key7 = "<stamina minimum deposit>"
    key8 = "<stamina epoch length>"
    key9 = "<stamina withdrawal delay>"
    key10 = "<chain id>"
    key11 = "<pre asset true or false>"
    key12 = "<epoch lenth of plasma>"
    key13 = "<node key hex>"
    key14 = "<rootchain ip address>"
    key15 = "<operator name>"
    key16 = "<website address>"
    key17 = "<description>"
    key18 = "<api server address>"
    key = [key1, key2, key3, key4, key5, key6, key7, key8, key9, key10, key11, key12, key13, key14, key15, key16, key17, key18]
    
    cmdg = "sed -i "
    
    for i in range(len(parameter) - 1):
        cmdg = cmdg + control_sed(key[i], parameter[i])
    cmd = cmdg + "/home/ubuntu/variables.list"

    # print(cmd)
    return ssh_execute(parameter[len(parameter) - 1], cmd)

def control_sed(key, parameter):
    return "-e 's/" + key + "/" + str(parameter) + "/g' "

def deploy_rootchain_contract(ip_address):
    return ssh_execute(host=ip_address, command="/home/ubuntu/1_deploy.rootchain.sh")

def export_genesis(ip_address):
    output = ssh_execute(host=ip_address, command="cat /home/ubuntu/genesis.json")
    print(output)
    return json.loads(output[0])

def initialize_operator_blockchain(ip_address):
    output = ssh_execute(host=ip_address, command="/home/ubuntu/2_init.oper.sh")
    return output

def managers_import(ip_address, managers):
    man = json.dumps(managers, indent=4)
    output = ssh_execute(host=ip_address, command="echo '" + man + "' | python3 -mjson.tool > /home/ubuntu/stake/manager.json")
    return output

def managers_set(ip_address):
    out = ssh_execute(host=ip_address, command="bash /home/ubuntu/stake/1_staking.set.manager.sh")
    return out

def managers_register(ip_address):
    out = ssh_execute(host=ip_address, command="bash /home/ubuntu/stake/2_register.manager.sh")
    return out

def operator_register(ip_address):
    out = ssh_execute(host=ip_address, command="bash /home/ubuntu/stake/3_register.rootchain.sh")
    return out

def run_operator(ip_address):
    return ssh_execute(host=ip_address, command="/home/ubuntu/3_run.operator.sh")

##############################
#### ROOTCHAIN CONTROLLER ####
##############################

def run_rootchain(ip_address):
    out = ssh_execute(host=ip_address, command="bash /home/ubuntu/run.rootchain.sh")
    print(out)
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
    out1 = json.loads(''.join(a))
    # out2 = json.dumps(out1, indent=4)
    return [out1]

def initialize_rootchain(ip_address):
    out = ssh_execute(host=ip_address, command="bash /home/ubuntu/reset.rootchain.sh")
    return out[0]

def change_rootchain_account(ip_address, key0, key1, key2, key3, key4, key5, operator, delay, seigniorage, p_round, password):
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
    op_password="<password>"

    cmdg = "sed -i "
    cmd0 = "-e 's/" + priv0 + "/" + key0 + "/g' "
    cmd1 = "-e 's/" + priv1 + "/" + key1 + "/g' "
    cmd2 = "-e 's/" + priv2 + "/" + key2 + "/g' "
    cmd3 = "-e 's/" + priv3 + "/" + key3 + "/g' "
    cmd4 = "-e 's/" + priv4 + "/" + key4 + "/g' "
    cmd5 = "-e 's/" + priv5 + "/" + key5 + "/g' "
    cmd6 = "-e 's/" + op + "/" + operator + "/g' "
    cmd7 = "-e 's/" + w_delay + "/" + str(delay) + "/g' "
    cmd8 = "-e 's/" + seig + "/" + str(seigniorage) + "/g' "
    cmd9 = "-e 's/" + round + "/" + str(p_round) + "/g' "
    cmd10 = "-e 's/" + op_password + "/" + password + "/g' "
    cmd11 = "/home/ubuntu/account.variable"

    cmd = cmdg + cmd0 + cmd1 + cmd2 + cmd3 + cmd4 + cmd5 + cmd6 + cmd7 + cmd8 + cmd9 + cmd10 + cmd11
    ssh_execute(ip_address, cmd)

##############################
#### USERNODE CONTROLLER  ####
##############################

def set_usernode_variable(user_ip, root_ip, operator_ip, enode_value, chain_id):
    key1 = "<rootchain ip>"
    key2 = "<operator ip>"
    key3 = "<enode value>"
    key4 = "<network id>"

    cmdg = "sed -i "
    cmd0 = "-e 's/" + key1 + "/" + root_ip + "/g' "
    cmd1 = "-e 's/" + key2 + "/" + operator_ip + "/g' "
    cmd2 = "-e 's/" + key3 + "/" + enode_value + "/g' "
    cmd3 = "-e 's/" + key4 + "/" + chain_id + "/g' "
    cmd4 = "/home/ubuntu/variables.list"

    cmd = cmdg + cmd0 + cmd1 + cmd2 + cmd3 + cmd4
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

############################
#### STAKING CONTROLLER ####
############################

def stake_ton(ip_address, prev_amount, amount):
    global staking_amount

    cmdg = "sed -i "
    cmd0 = "-e 's/" + staking_amount + "/" + amount + "/g' "
    cmd1 = "/home/ubuntu/variables.list"

    cmd = cmdg + cmd0 + cmd1
    ssh_execute(ip_address, cmd)
    # using db
    staking_amount = amount

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
