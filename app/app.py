import configparser
import paramiko
import boto3
import time
import sys

config = configparser.RawConfigParser()
config.read('config.ini')

from io import StringIO
from tinydb import TinyDB, Query
from tinydb.operations import delete, set
from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash
from flask_cors import CORS

from tokamak_aws import \
    get_instance_ip, \
    run_rootchain, \
    deploy_manager_contract, \
    deploy_powerton_contract, \
    start_powerton_contract, \
    export_manager_command, \
    export_manager_contract, \
    get_instance_resource, \
    ssh_execute, \
    change_rootchain_account, \
    initialize_rootchain, \
    create_instance, \
    change_account_operator, \
    deploy_rootchain_contract, \
    export_genesis, \
    initialize_operator_blockchain, \
    run_operator, \
    managers_import, \
    managers_set, \
    managers_register, \
    operator_register, \
    get_log_tail, \
    set_usernode_variable, \
    import_genesis_usernode, \
    check_genesis, \
    initialize_usernode, \
    run_usernode, \
    create_pem, \
    delete_pem, \
    config_set
    

from utilities.update_instance import update_operator, update_rootchain, update_usernode
from utilities.network_generator import get_network_json
from utilities.get_web3 import get_balance



DEBUG = config["SERVER"]["DEBUG"]
SECRET_KEY = config["SERVER"]["SECRET_KEY"]
USERNAME = config["SERVER"]["USERNAME"]
PASSWORD = config["SERVER"]["PASSWORD"]
PEMFILE = config["SSH"]["SSH_PEMFILE"]
SSH_USERNAME = config["SSH"]["SSH_USERNAME"]

t_db = TinyDB(config["DATABASE"]["DATABASE"])

sample_page = Blueprint('sample_page', 'sample_page', template_folder='templates')


app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)


@app.route("/home")
def home():
    network = get_network_json()
    return network

#####################
### CONFIG ROUTE ####
#####################

@app.route("/config", methods=["GET"])
def config_router():
    target = {}

    for i in config.items():
        for j in i[1].keys():
            target[j] = config[i[0]][j]

    return target
        

@app.route("/config/pem/form")
def pem_router():
    pems = t_db.search(Query().Type == "pem")
    
    return pems

@app.route("/config/pem/form/create", methods=["POST"])
def pem_create():
    error = None
    res = []
    output_stream = StringIO

    if request.method == 'POST':
        req = request.get_json(force=True)
        name = req['name']
        try:
            key_pair, key_finger_print = create_pem(name)
            outfile = open('./.pem/' + name + '.pem','w+')
            outfile.write(key_pair)
        except Exception as e:
            flash([str(e)])
            return redirect(url_for('pem_router'))

        inst_obj = {
            'Type' : "pem",
            'Name' : name,
            'FingerPrint': key_finger_print,
        }

        t_db.insert(inst_obj)
        q_res = t_db.search(Query().Name == name)
        flash([str(q_res), "Pem Created!"])
        return redirect(url_for('pem_router'))
    else:
        return url_for('pem_router')

@app.route("/config/pem/form/delete", methods=["DELETE"])
def pem_delete():
    if request.method == 'DELETE':
        pem_list = []        
        name = request.args['name']        
        pem_list = name.split(',')
        
        try:
            for i in range(len(pem_list)):
                response = delete_pem(pem_list[i])
                flash(response)
                t_db.remove(Query()['Name']==pem_list[i])
            
        except Exception as e:
            flash([str(e)])
            return redirect(url_for('pem_router'))

        return redirect(url_for('pem_router'))

@app.route("/config/set", methods=["POST"])
def config_ini_set():              
    if request.method == 'POST':
        req = request.get_json(force=True)
        parameter={
            'ac_key' : req['AccessKey'],
            'sec_key' : req['AwsSecretKey'],

            'img_id' : req['ImageID'],
            'ins_type' : req['InstanceType'],
            'sec_group_id' : req['SecurityGroupID'],
            'key_name' : req['KeyName'],
            'region_name' : req['RegionName'],

            'ssh_user' : req['SshUsername'],
            'ssh_pem' : req['SshPemfile'],

            'debug' : req['Debug'],
            'secret_key' : req['SecretKey'],
            'username' : req['Username'],
            'password' : req['Password'],
            'database' : req['Database'],
        }

        #put into config.ini
        config.set('AWS','AWS_ACCESS_KEY', parameter['ac_key'])
        config.set('AWS','AWS_SECRET_KEY', parameter['sec_key'])

        config.set('INSTANCE', 'BASIC_IMAGE_ID', parameter['img_id'])
        config.set('INSTANCE', 'INSTANCE_TYPE', parameter['ins_type'])
        config.set('INSTANCE', 'SECURITY_GROUP_ID', parameter['sec_group_id'])
        config.set('INSTANCE','KEY_NAME', parameter['key_name'])
        config.set('INSTANCE','REGION_NAME', parameter['region_name'])

        config.set('SSH','SSH_USERNAME', parameter['ssh_user'])
        config.set('SSH','SSH_PEMFILE', parameter['ssh_pem'])

        config.set('SERVER','DEBUG', parameter['debug'])
        config.set('SERVER','SECRET_KEY', parameter['secret_key'])
        config.set('SERVER','USERNAME', parameter['username'])
        config.set('SERVER','PASSWORD', parameter['password'])

        config.set('DATABASE','DATABASE', parameter['database'])

        with open('config.ini', 'w+') as configfile:
            config.write(configfile)

    global DEBUG, SECRET_KEY, USERNAME, PASSWORD, PEMFILE, SSH_USERNAME
    DEBUG = parameter['debug']
    SECRET_KEY = parameter['secret_key']
    USERNAME = parameter['username']
    PASSWORD = parameter['password']
    PEMFILE = parameter['ssh_pem']
    SSH_USERNAME = parameter['ssh_user']

    config_set(parameter)
    config.read('config.ini')
    flash([time.ctime()[11:19] + " config.ini set!"])

    return redirect(url_for('config_router'))


#####################
## ROOTCHAIN ROUTE ##
#####################

@app.route("/rootchain", methods=["GET"])
def rootchain():
    data = t_db.search(Query().Type == "rootchain")
    value = {}
    for i in range(len(data)):
        value[i] = data[i]
    # if data == "":
    #     data = []
    # print(value)
    return value


@app.route("/rootchain/startnode", methods=["POST"])
def rootchain_start():
    error = None
    if request.method == "POST":
        req = request.get_json(force=True)
        inst_id = req['instance_id']
        inst = t_db.search(Query().InstanceId == inst_id)[0]
        inst_faucet = inst['Faucet']
        inst_ip = inst['IpAddress']

        #change account
        change_rootchain_account(
            inst_ip,
            inst_faucet[0],
            inst_faucet[1],
            inst_faucet[2],
            inst_faucet[3],
            inst_faucet[4],
            inst_faucet[5],
            inst['Operator'],
            inst['Staking']['WithdrawalDelay'],
            inst['Staking']['SeigPerBlock'],
            inst['Staking']['PwertTONRoundTime'],
            inst['OperatorPassword']
        )

        #run rootchain node
        run_rootchain(inst_ip)
        #update database
        t_db.update(set('Status', 'mining'), Query().InstanceId == inst_id)
        #flash
        flash([time.ctime()[11:19] + " Rootchain Mining Started!"])
        return redirect(url_for('rootchain'))
    else:
        return redirect(url_for('rootchain'))

@app.route("/rootchain/reset", methods=["POST"])
def rootchain_reset():
    error = None
    if request.method == "POST":
        req = request.get_json(force=True)
        inst_id = req['instance_id']
        inst = t_db.search(Query().InstanceId == inst_id)[0]
        inst_ip = inst['IpAddress']
        initialize_rootchain(inst_ip)
        #flash
        flash([time.ctime()[11:19] + " Rootchain Reset!"])
        return redirect(url_for('rootchain'))
    else:
        return redirect(url_for('rootchain'))

@app.route("/rootchain/create", methods=["POST"])
def rootchain_create():
    error = None
    res = []
    if request.method == 'POST':
        req = request.get_json(force=True)
        name = req['Name']
        key0 = req['Key1']
        key1 = req['Key2']
        key2 = req['Key3']
        key3 = req['Key4']
        key4 = req['Key5']
        key5 = req['Key6']

        key1address = req['Key1Address']
        key1password = req['Password']
        withdrawal_delay = req['WithdrawalDelay']
        seig_per_block = req['Seigniorage']
        power_ton_round_time = req['PowerTONRound']

        root_ins = create_instance(name)
        root_ins_monitor = root_ins.monitor()
        inst_obj = {
            'Type' : "rootchain",
            'Name' : name,
            'InstanceId' : root_ins_monitor['InstanceMonitorings'][0]['InstanceId'],
            'Status' : root_ins_monitor['InstanceMonitorings'][0]['Monitoring']['State'],
            'Date' : root_ins_monitor['ResponseMetadata']['HTTPHeaders']['date'],
            'Faucet' : [key0, key1, key2, key3, key4, key5],
            'Operator' : key1address,
            'OperatorPassword' : key1password,
            'Staking' : {
                'WithdrawalDelay' : withdrawal_delay,
                'SeigPerBlock' : seig_per_block,
                'PwertTONRoundTime' : power_ton_round_time
                },
            'IsScriptSet' : '',
            'IsMansgerDeployed' : '',
            'IsPowerTONDeployed' : '',
            'IsPowerTONStarted' : '',
            'IsManagerExported': '',
            'Managers' : "",
            'Managers2' : ""
        }
        t_db.insert(inst_obj)
        q_res = t_db.search(Query().Name == name)
        flash([str(q_res), "Rootchain Created!"]);
        return redirect(url_for('rootchain'))
    else:
        return url_for('rootchain')

@app.route("/rootchain/deploy/manager/<instanceid>")
def deploy_manager(instanceid):
    inst = t_db.search(Query().InstanceId == instanceid)

    inst_ip = inst[0]["IpAddress"]
    inst_id = inst[0]["InstanceId"]
    inst_type = inst[0]["Type"]

    out = deploy_manager_contract(inst_ip)
    t_db.update(set('IsMansgerDeployed', "true"), Query().InstanceId == inst_id)
    flash(out)

    return redirect(url_for('rootchain'))

@app.route("/rootchain/deploy/powerton/<instanceid>")
def deploy_powerton(instanceid):
    inst = t_db.search(Query().InstanceId == instanceid)
    inst_ip = inst[0]["IpAddress"]
    inst_id = inst[0]["InstanceId"]
    inst_type = inst[0]["Type"]

    out = deploy_powerton_contract(inst_ip)
    t_db.update(set('IsPowerTONDeployed', "true"), Query().InstanceId == inst_id)
    flash(out)

    return redirect(url_for('rootchain'))

@app.route("/rootchain/start/powerton/<instanceid>")
def start_powerton(instanceid):
    inst = t_db.search(Query().InstanceId == instanceid)
    inst_ip = inst[0]["IpAddress"]
    inst_id = inst[0]["InstanceId"]
    inst_type = inst[0]["Type"]

    out = start_powerton_contract(inst_ip)
    t_db.update(set('IsPowerTONStarted', "true"), Query().InstanceId == inst_id)
    flash(out)

    return redirect(url_for('rootchain'))

@app.route("/rootchain/export/manager/<instanceid>")
def export_manager(instanceid):
    inst = t_db.search(Query().InstanceId == instanceid)
    inst_ip = inst[0]["IpAddress"]
    inst_id = inst[0]["InstanceId"]
    inst_type = inst[0]["Type"]

    export_manager_command(inst_ip)
    out = export_manager_contract(inst_ip)
    t_db.update(set('Managers', out[0]), Query().InstanceId == inst_id)
    t_db.update(set('IsManagerExported', 'true'), Query().InstanceId == inst_id)
    flash(out)

    return redirect(url_for('rootchain'))

####################
## OPERATOR ROUTE ##
####################

@app.route("/operator")
def operator():
    data = t_db.search(Query().Type == "operator")
    value = {}
    for i in range(len(data)):
        value[i] = data[i]

    return value

@app.route("/operator/form")
def operator_form():
    data = t_db.search(Query().Type == "rootchain")
    return render_template(
            "operator/operator_create.html",
            data = data
        );

@app.route("/operator/form/create", methods=["POST"])
def operator_create():
    error = None
    res = []
    if request.method == 'POST':
        req = request.get_json(force=True)
        name = req['Name']
        chainid = req["ChainID"]
        epoch = req["Epoch"]
        pre_asset = req["PreAsset"]
        rootchain_id = req['RootchainID']
        node_key = req['Nodekey']
        operator_account = req['OperatorAccount']
        operator_account_key = req['OperatorAccountKey']
        operator_password = req['OperatorPassword']
        deploy_gasprice = req['DeployGasprice']
        commit_gasprice = req['CommitGasprice']
        stamina_operator_amount = req['StaminaOperatorAmount']
        stamina_min_deposit = req['StaminaMinDeposit']
        stamina_recover_epoch_length = req['StaminaRecoverEpochLength']
        stamina_withdrawal_delay = req['StaminaWithdrawalDelay']
        website = req['Website']
        description = req['Description']
        api_server = req['ApiServer']

        print("##################", pre_asset)

        if req["PreAsset"] == 'on':
            pre_asset = "true"
        else :
            pre_asset = "false"
        
        root_inst = t_db.search(Query().InstanceId == rootchain_id)[0]

        operator_ins = create_instance(name)
        operator_ins_monitor = operator_ins.monitor()
        inst_obj = {
            'Type' : "operator",
            'Name' : name,
            'ChainID' : chainid,
            'Epoch' : epoch,
            'PreAsset' : pre_asset,
            'RootChain' : {
                'Name': root_inst["Name"],
                "IpAddress":root_inst["IpAddress"],
                "InstanceId":rootchain_id
            },
            'InstanceId' : operator_ins_monitor['InstanceMonitorings'][0]['InstanceId'],
            'Status' : operator_ins_monitor['InstanceMonitorings'][0]['Monitoring']['State'],
            'Date' : operator_ins_monitor['ResponseMetadata']['HTTPHeaders']['date'],
            'RootchainId' : rootchain_id,
            'NodeKey' : node_key,
            'OperatorAccount' : operator_account,
            'OperatorAccountKey' : operator_account_key,
            'OperatorPassword' : operator_password,
            'DeployGasprice': deploy_gasprice,
            'CommitGasprice': commit_gasprice,
            'Stamina': {
                'OperatorAmount': stamina_operator_amount,
                'MinDeposit': stamina_min_deposit,
                'RecoverEpochLength': stamina_recover_epoch_length,
                'WithdrawalDelay': stamina_withdrawal_delay,
            },
            'Dashboard': {
                'OperatorName' : name,
                'Website' : website,
                'Description' : description,
                'ApiServer' : api_server,
            },
            'Staking': {
                'OperatorStaked': '',
                'TotalStaked': '',
                'PrevStake': '',
                'PrevUnstake': '',
                'AvailableAmount': '',
                'TonBalance': '',
                'PethBalance': '',
            },
            'IsSet' : '',
            'IsDeployed' : '',
            'Genesis' : '',
            'IsExported' : '',
            'IsInitialized' : '',
            'IsManagersImported' : '',
            'IsManagersSet' : '',
            'IsMansgersRegistered' : '',
            'IsOperatorRegistered' : ''
        }
        t_db.insert(inst_obj)
        q_res = t_db.search(Query().Name == name)
        flash([str(q_res), "Operator Instance Created!"])
        return redirect(url_for('operator'))
    else:
        return url_for('operator')


@app.route("/operator/set/variable", methods=["POST"])
def operator_set_variable():
    error = None
    res = []
    if request.method == 'POST':
        req = request.get_json(force=True)
        inst_id = req["instance_id"]
        inst = t_db.search(Query().InstanceId == inst_id)[0]

        parameter = [
            inst['OperatorAccountKey'],
            inst['OperatorAccount'],
            inst['OperatorPassword'],
            inst['DeployGasprice'],
            inst['CommitGasprice'],
            inst['Stamina']['OperatorAmount'],
            inst['Stamina']['MinDeposit'],
            inst['Stamina']['RecoverEpochLength'],
            inst['Stamina']['WithdrawalDelay'],
            inst['ChainID'],
            inst['PreAsset'],
            inst['Epoch'],
            inst['NodeKey'],
            inst['RootChain']["IpAddress"],
            inst['Dashboard']['OperatorName'],
            inst['Dashboard']['Website'],
            inst['Dashboard']['Description'],
            inst['Dashboard']['ApiServer'],
            inst["IpAddress"],
        ]
        
        res = change_account_operator(parameter)
        t_db.update(set('IsSet', "true"), Query().InstanceId == inst_id)
        flash([time.ctime()[11:19] + " Operator Variable Set!"])
        return redirect(url_for('operator'))
    else:
        return redirect(url_for('operator'))

@app.route("/operator/deploy/rootchain", methods=["POST"])
def operator_deploy_rootchain():
    error = None
    res = []
    if request.method == 'POST':
        req = request.get_json(force=True)
        inst_id = req["instance_id"]
        inst = t_db.search(Query().InstanceId == inst_id)[0]
        inst_ip = inst['IpAddress']
        out1 = deploy_rootchain_contract(inst_ip)
        t_db.update(set('IsDeployed', "true"), Query().InstanceId == inst_id)
        # flash([time.ctime()[11:19] + " rootchain contract deployed!"])
        flash(out1)
        return redirect(url_for('operator'))
    else:
        return redirect(url_for('operator'))

@app.route("/operator/export/genesis", methods=["POST"])
def operator_export_genesis():
    error = None
    res = []
    if request.method == 'POST':
        req = request.get_json(force=True)
        inst_id = req["instance_id"]
        inst = t_db.search(Query().InstanceId == inst_id)[0]
        
        genesis = export_genesis(inst["IpAddress"])
        t_db.update(set('Genesis', genesis), Query().InstanceId == inst_id)
        t_db.update(set('IsExported', "true"), Query().InstanceId == inst_id)
        flash([time.ctime()[11:19] + " genesis.json exported! --> "+str(genesis)])
        return redirect(url_for('operator'))
    else:
        return redirect(url_for('operator'))

@app.route("/operator/initialize", methods=["POST"])
def operator_initialize():
    error = None
    res = []
    if request.method == 'POST':
        req = request.get_json(force=True)
        inst_id = req["instance_id"]
        inst = t_db.search(Query().InstanceId == inst_id)[0]
        # TODO : initialize operator
        out = initialize_operator_blockchain(inst["IpAddress"])
        t_db.update(set('IsInitialized', "true"), Query().InstanceId == inst_id)
        flash([time.ctime()[11:19] + " Operator Initialized!"])
        return redirect(url_for('operator'))
    else:
        return redirect(url_for('operator'))

@app.route("/operator/import/managers/<instanceid>")
def operator_import_managers(instanceid):
    inst = t_db.search(Query().InstanceId == instanceid)
    inst_ip = inst[0]["IpAddress"]

    #get managers json data
    root_id = inst[0]['RootChain']['InstanceId']
    root_inst = t_db.search(Query().InstanceId == root_id)
    managers = root_inst[0]["Managers"]

    #import managers.json to operator node
    out = managers_import(inst_ip, managers)
    t_db.update(set('IsManagersImported', "true"), Query().InstanceId == instanceid)
    flash([time.ctime()[11:19] + " managers.json imported!"])
    return redirect(url_for('operator'))


@app.route("/operator/set/managers/<instanceid>")
def operator_set_managers(instanceid):
    inst = t_db.search(Query().InstanceId == instanceid)
    inst_ip = inst[0]["IpAddress"]

    # set managers
    out = managers_set(inst_ip)

    # update db
    t_db.update(set('IsManagersSet', "true"), Query().InstanceId == instanceid)

    flash(out)
    return redirect(url_for('operator'))

@app.route("/operator/register/managers/<instanceid>")
def operator_register_managers(instanceid):
    inst = t_db.search(Query().InstanceId == instanceid)
    inst_ip = inst[0]["IpAddress"]

    out = managers_register(inst_ip)
    t_db.update(set('IsManagersRegistered', "true"), Query().InstanceId == instanceid)

    flash(out)
    return redirect(url_for('operator'))

@app.route("/operator/register/rootchain/<instanceid>")
def dashboard_register_managers(instanceid):
    inst = t_db.search(Query().InstanceId == instanceid)
    inst_ip = inst[0]["IpAddress"]

    out = operator_register(inst_ip)
    t_db.update(set('IsManagersRegistered', "true"), Query().InstanceId == instanceid)

    flash(out)
    return redirect(url_for('operator'))

@app.route("/operator/runnode", methods=["POST"])
def operator_runnode():
    error = None
    res = []
    if request.method == 'POST':
        req = request.get_json(force=True)
        inst_id = req["instance_id"]
        inst = t_db.search(Query().InstanceId == inst_id)[0]
        out = run_operator(inst["IpAddress"])
        t_db.update(set('Status', "mining"), Query().InstanceId == inst_id)
        flash([time.ctime()[11:19] + " Operator Running!"])
        return redirect(url_for('operator'))
    else:
        return redirect(url_for('operator'))

#######################
## USERNODE SETTING ###
#######################

@app.route("/usernode")
def usernode():
    data = t_db.search(Query().Type == "usernode")
    value = {}
    for i in range(len(data)):
        value[i] = data[i]
        
    return value

@app.route("/usernode/form")
def usernode_form():
    data = t_db.search(Query().Type == "rootchain")
    data2 = t_db.search(Query().Type == "operator")
    return render_template(
            "usernode/usernode_create.html",
            data = data,
            data2 = data2
        );

@app.route("/usernode/form/create", methods=["POST"])
def usernode_create():
    error = None
    res = []
    if request.method == 'POST':
        req = request.get_json(force=True)
        name = req['Name']
        rootchain_id = req['RootchainID']
        operator_id = req['OperatorID']
        enode_hex = req['enodehex']

        root_inst = t_db.search(Query().InstanceId == rootchain_id)[0]
        operator_inst = t_db.search(Query().InstanceId == operator_id)[0]

        usernode_ins = create_instance(name)
        usernode_ins_monitor = usernode_ins.monitor()

        inst_obj = {
            'Type' : "usernode",
            'Name' : name,
            'RootChain' : {
                'Name': root_inst["Name"],
                "IpAddress":root_inst["IpAddress"],
                "InstanceId":rootchain_id
            },
            'Operator' : {
                'Name': operator_inst["Name"],
                "IpAddress": operator_inst["IpAddress"],
                "InstanceId": operator_inst["InstanceId"],
                "Genesis" : operator_inst["Genesis"],
                "ChainID" : operator_inst["ChainID"]
            },
            'InstanceId' : usernode_ins_monitor['InstanceMonitorings'][0]['InstanceId'],
            'Status' : usernode_ins_monitor['InstanceMonitorings'][0]['Monitoring']['State'],
            'Date' : usernode_ins_monitor['ResponseMetadata']['HTTPHeaders']['date'],
            'Enode' : enode_hex,
            'IsInitialized' : ''
        }
        t_db.insert(inst_obj)
        q_res = t_db.search(Query().Name == name)
        flash([str(q_res), "User Node Instance Created!"]);
        return redirect(url_for('usernode'))
    else:
        return url_for('usernode')

@app.route("/usernode/initialize", methods=["POST"])
def usernode_initialize():
    error = None
    res = []
    if request.method == 'POST':
        req = request.get_json(force=True)
        inst_id = req["instance_id"]
        user_inst = t_db.search(Query().InstanceId == inst_id)[0]

        #set variable
        user_ip = user_inst["IpAddress"]
        rootchain_ip = user_inst["RootChain"]["IpAddress"]
        chain_id = user_inst["Operator"]["ChainID"]
        operator_ip = user_inst["Operator"]["IpAddress"]
        enode_value = user_inst["Enode"]
        out1 = set_usernode_variable(user_ip, rootchain_ip, operator_ip, enode_value, chain_id)
        # print("out1 : ", out1)

        # import genesis to usernode
        genesis = user_inst["Operator"]["Genesis"]
        out2 = import_genesis_usernode(user_ip, genesis)
        check_genesis(user_ip)
        # print("out1 : ", out2)

        #initialize usernode
        initialize_usernode(user_ip)
        t_db.update(set('IsInitialized', "true"), Query().InstanceId == inst_id)
        flash([time.ctime()[11:19] + " Usernode Initialized!"])
        return redirect(url_for('usernode'))
    else:
        return redirect(url_for('usernode'))

@app.route("/usernode/runnode", methods=["POST"])
def usernode_runnode():
    error = None
    res = []
    if request.method == 'POST':
        req = request.get_json(force=True)
        inst_id = req["instance_id"]
        inst = t_db.search(Query().InstanceId == inst_id)[0]
        out = run_usernode(inst["IpAddress"])
        print(out)
        t_db.update(set('Status', "mining"), Query().InstanceId == inst_id)
        flash([time.ctime()[11:19] + " User Node Running!"])
        return redirect(url_for('usernode'))
    else:
        return redirect(url_for('usernode'))


#######################
### STAKING SETTING ###
#######################

@app.route("/staking")
def staking():
    data = t_db.search(Query().Type == "operator")
    for i in range(len(data)):
        operator_staked, total_staked = get_balance(data[i]['OperatorAccount']) # ToDo: connect to web3
        data[i]['Staking']['OperatorStaked'] = operator_staked
        data[i]['Staking']['TotalStaked'] = total_staked

    return render_template(
            "staking/staking_operator_list.html",
            data = data
        );

@app.route("/staking/info/<instanceid>")
def staking_info(instanceid):
    res = t_db.search(Query().InstanceId == instanceid)
    
    # inst['Balance']['TON']
    
    return render_template(
        "staking/staking_operator_info.html",
        data = res
    )

@app.route("/staking/info/<instanceid>/stake/<amount>")
def stake(instanceid, amount):
    res = t_db.search(Query().InstanceId == instanceid)
    # res['Staking']


# @app.route("/staking/form")
# def usernode_form():
#     data = t_db.search(Query().Type == "rootchain")
#     data2 = t_db.search(Query().Type == "operator")
#     return render_template(
#             "usernode/usernode_create.html",
#             data = data,
#             data2 = data2
#         );



#####################
## INSTANCE ROUTE ###
#####################

@app.route("/instance/<instanceid>")
def instance(instanceid):
    res = t_db.search(Query().InstanceId == instanceid)
    # print(instanceid)
    return render_template(
            "instance/instance.html",
            data = res[0]
        );

@app.route("/instance/reset/<instanceid>")
def reset_instance(instanceid):
    inst = t_db.search(Query().InstanceId == instanceid)
    inst_ip = inst[0]["IpAddress"]
    inst_name = inst[0]["Name"]
    inst_type = inst[0]["Type"]

    if inst_type == "rootchain":
        update_rootchain(inst_ip, SSH_USERNAME, PEMFILE)
        t_db.update(set('Status', "enabled"), Query().InstanceId == instanceid)
        t_db.update(set('IsScriptSet', "true"), Query().InstanceId == instanceid)
        t_db.update(set('IsMansgerDeployed', ""), Query().InstanceId == instanceid)
        t_db.update(set('IsPowerTONDeployed', ""), Query().InstanceId == instanceid)
        t_db.update(set('IsPowerTONStarted', ""), Query().InstanceId == instanceid)
        t_db.update(set('Managers', ""), Query().InstanceId == instanceid)
        t_db.update(set('IsManagerExported', ""), Query().InstanceId == instanceid)
        flash([time.ctime()[11:19] + " " + inst_name + " reset"])
        return redirect(url_for('rootchain'))
    elif inst_type == "operator":
        update_operator(inst_ip, SSH_USERNAME, PEMFILE)
        t_db.update(set('Status', "enabled"), Query().InstanceId == instanceid)
        t_db.update(set('IsScriptSet', "true"), Query().InstanceId == instanceid)
        t_db.update(set('IsSet', ""), Query().InstanceId == instanceid)
        t_db.update(set('IsDeployed', ""), Query().InstanceId == instanceid)
        t_db.update(set('Genesis', ""), Query().InstanceId == instanceid)
        t_db.update(set('IsExported', ""), Query().InstanceId == instanceid)
        t_db.update(set('IsInitialized', ""), Query().InstanceId == instanceid)
        t_db.update(set('IsManagersImported', ""), Query().InstanceId == instanceid)
        t_db.update(set('IsManagersSet', ""), Query().InstanceId == instanceid)
        t_db.update(set('IsManagersRegistered', ""), Query().InstanceId == instanceid)
        flash([time.ctime()[11:19] + " " + inst_name + " reset"])
        return redirect(url_for('operator'))
    elif inst_type == "usernode":
        update_usernode(inst_ip, SSH_USERNAME, PEMFILE)
        t_db.update(set('Status', "enabled"), Query().InstanceId == instanceid)
        t_db.update(set('IsScriptSet', "true"), Query().InstanceId == instanceid)
        t_db.update(set('IsInitialized', ""), Query().InstanceId == instanceid)
        flash([time.ctime()[11:19] + " " + inst_name + " reset"])
        return redirect(url_for('usernode'))


@app.route("/instance/<instanceid>/<filename>")
def log(instanceid, filename):
    inst = t_db.search(Query().InstanceId == instanceid)
    inst_ip = inst[0]["IpAddress"]
    inst_type = inst[0]["Type"]
    log = get_log_tail(inst_ip, filename)
    # print(log)
    flash(log)
    if inst_type == "rootchain":
        return redirect(url_for('rootchain'))
    elif inst_type == "operator":
        return redirect(url_for('operator'))
    elif inst_type == "usernode":
        return redirect(url_for('usernode'))

@app.route("/instance/terminate", methods=["POST"])
def instance_terminate():
    error = None
    res = []
    if request.method == 'POST':
        req = request.get_json(force=True)
        inst_id = req['instance_id']
        inst = t_db.search(Query().InstanceId == inst_id)[0]
        inst_ip = inst['IpAddress']
        #terminate instance
        inst_res = get_instance_resource(inst_id)
        terminate_out = inst_res.terminate()
        #update database from something to shutdown
        t_db.update(set('Status', "shutdown"), Query().InstanceId == inst_id)

        flash([time.ctime()[11:19] + " " + inst_id + " terminated..."])

        if inst['Type'] == "rootchain":
            return redirect(url_for('rootchain'))
        elif inst['Type'] == "operator":
            return redirect(url_for('operator'))
        elif inst['Type'] == "usernode":
            return redirect(url_for('usernode'))

    else:
        return url_for('rootchain')


@app.route("/check/status", methods=["POST"])
def check_status():
    error = None
    if request.method == "POST":
        req = request.get_json(force=True)
        inst_id = req['instance_id']
        inst = t_db.search(Query().InstanceId == inst_id)[0]
        # TODO : CHECK STATUS - Pending | enable | mining | dead
        prior_status = t_db.search(Query().InstanceId == inst_id)[0]['Status']

        inst_resource = get_instance_resource(inst_id)
        inst_monitor = inst_resource.monitor()
        status = inst_monitor['InstanceMonitorings'][0]['Monitoring']['State']
        #Check if prior status is mining, let it be
        if prior_status == "mining":
            status = prior_status
        else:
            t_db.update(set('Status', status), Query().InstanceId == inst_id)
        # return by Type of data : rootchain | operator | usernode
        flash([time.ctime()[11:19] + " Status Checked(" + prior_status + " --> " + status+')!'])
        if inst['Type'] == "rootchain":
            return redirect(url_for('rootchain'))
        elif inst['Type'] == "operator":
            return redirect(url_for('operator'))
        elif inst['Type'] == "usernode":
            return redirect(url_for('usernode'))
    else:
        return redirect(url_for('rootchain'))

@app.route("/check/ip", methods=["POST"])
def check_ip():
    error = None
    if request.method == "POST":
        req = request.get_json(force=True)
        inst_id = req['instance_id']
        inst = t_db.search(Query().InstanceId == inst_id)[0]
        # TODO : CHECK STATUS - Pending | running | mining | shotdown
        inst_ip = get_instance_ip(inst_id)
        t_db.update(set('IpAddress', inst_ip), Query().InstanceId == inst_id)
        # return by Type of data : rootchain | operator | usernode
        flash([time.ctime()[11:19] + " Capture IP Address of " + inst_id])
        if inst['Type'] == "rootchain":
            return redirect(url_for('rootchain'))
        elif inst['Type'] == "operator":
            return redirect(url_for('operator'))
        elif inst['Type'] == "usernode":
            return redirect(url_for('usernode'))
    else:
        return redirect(url_for('rootchain'))


@app.route("/dropdata", methods=["POST"])
def drop_data():
    error = None
    if request.method == "POST":
        req = request.get_json(force=True)
        inst_id = req['instance_id']
        inst = t_db.search(Query().InstanceId == inst_id)[0]
        #TODO : if it is not in a "Shutdown" status, it should not work
        if not inst["Status"] == "shutdown":
            flash([time.ctime()[11:19] + " " + inst_id + " does not in 'shutdown' status"])
            if inst['Type'] == "rootchain":
                return redirect(url_for('rootchain'))
            elif inst['Type'] == "operator":
                return redirect(url_for('operator'))
        #delete database row
        t_db.remove(Query().InstanceId == inst_id)

        flash([time.ctime()[11:19] + " " + inst_id + " Removed"])

        if inst['Type'] == "rootchain":
            return redirect(url_for('rootchain'))
        elif inst['Type'] == "operator":
            return redirect(url_for('operator'))
        elif inst['Type'] == "usernode":
            return redirect(url_for('usernode'))
    else:
        return redirect(url_for('rootchain'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
