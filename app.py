import configparser
import paramiko
import boto3
import time
import sys

config = configparser.ConfigParser()
config.read('config.ini')

from tinydb import TinyDB, Query
from tinydb.operations import delete, set
from flask import Flask, render_template, request, redirect, url_for, flash
from tokamak_aws import create_rootchain_instance, \
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
    create_operator_instance, \
    change_account_operator, \
    deploy_rootchain_contract, \
    export_genesis, \
    initialize_operator_blockchain, \
    run_operator, \
    restart_operator,\
    managers_import, \
    managers_set, \
    managers_register, \
    get_log_tail, \
    create_usernode_instance, \
    set_usernode_variable, \
    import_genesis_usernode, \
    check_genesis, \
    initialize_usernode, \
    run_usernode

DEBUG = config["SERVER"]["DEBUG"]
SECRET_KEY = config["SERVER"]["SECRET_KEY"]
USERNAME = config["SERVER"]["USERNAME"]
PASSWORD = config["SERVER"]["PASSWORD"]

t_db = TinyDB(config["DATABASE"]["DATABASE"])

app = Flask(__name__)
app.config.from_object(__name__)

#####################
## ROOTCHAIN ROUTE ##
#####################

@app.route("/rootchain")
def rootchain():
    data = t_db.search(Query().Type == "rootchain")
    if data == "":
        data = []
    # print(data)
    return render_template(
            "rootchain_list.html",
            data = data
        );

@app.route("/rootchain/startnode", methods=["POST"])
def rootchain_start():
    error = None
    if request.method == "POST":
        inst_id = request.form['instance_id']
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
        inst_id = request.form['instance_id']
        inst = t_db.search(Query().InstanceId == inst_id)[0]
        inst_ip = inst['IpAddress']
        initialize_rootchain(inst_ip)
        #flash
        flash([time.ctime()[11:19] + " Rootchain Reset!"])
        return redirect(url_for('rootchain'))
    else:
        return redirect(url_for('rootchain'))


@app.route("/rootchain/form")
def rootchain_form():
    return render_template(
            "rootchain_create_form.html"
        );

@app.route("/rootchain/form/create", methods=["POST"])
def rootchain_create():
    error = None
    res = []
    if request.method == 'POST':
        name = request.form['Name']
        key0 = request.form['Key1']
        key1 = request.form['Key2']
        key2 = request.form['Key3']
        key3 = request.form['Key4']
        key4 = request.form['Key5']
        key5 = request.form['Key6']

        key1address = request.form['Key1Address']
        key1password = request.form['Password']
        withdrawal_delay = request.form['WithdrawalDelay']
        seig_per_block = request.form['Seigniorage']
        power_ton_round_time = request.form['PowerTONRound']

        root_ins = create_rootchain_instance(name)
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
            'IsMansgerDeployed' : 'false',
            'IsPowerTONDeployed' : 'false',
            'IsPowerTONStarted' : 'false',
            'IsManagerExported': 'false',
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

#####################
## OPERATOR ROUTE ##
#####################

@app.route("/operator")
def operator():
    data = t_db.search(Query().Type == "operator")
    # print(data)
    return render_template(
            "operator_list.html",
            data = data
        );

@app.route("/operator/form")
def operator_form():
    data = t_db.search(Query().Type == "rootchain")
    return render_template(
            "operator_create_form.html",
            data = data
        );

@app.route("/operator/form/create", methods=["POST"])
def operator_create():
    error = None
    res = []
    if request.method == 'POST':
        name = request.form['Name']
        chainid = request.form["ChainID"]
        epoch = request.form["Epoch"]
        pre_asset = request.form["PreAsset"]
        rootchain_id = request.form['RootchainID']
        node_key = request.form['Nodekey']
        operator_account = request.form['OperatorAccount']
        operator_account_key = request.form['OperatorAccountKey']
        operator_password = request.form['OperatorPassword']

        print("##################", pre_asset)

        if request.form["PreAsset"] == 'on':
            pre_asset = "true"
        else :
            pre_asset = "false"

        root_inst = t_db.search(Query().InstanceId == rootchain_id)[0]

        operator_ins = create_operator_instance(name)
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
            'IsManagersImported' : '',
            'IsManagersSet' : '',
            'IsMansgersRegistered' : ''
        }
        t_db.insert(inst_obj)
        q_res = t_db.search(Query().Name == name)
        flash([str(q_res), "Operator Instance Created!"]);
        return redirect(url_for('operator'))
    else:
        return url_for('operator')


@app.route("/operator/set/variable", methods=["POST"])
def operator_set_variable():
    error = None
    res = []
    if request.method == 'POST':
        inst_id = request.form["instance_id"]
        inst = t_db.search(Query().InstanceId == inst_id)[0]
        op_ip = inst["IpAddress"]
        op_key = inst['OperatorAccountKey']
        op_addrs = inst['OperatorAccount']
        op_pass = inst['OperatorPassword']
        chain_id = inst['ChainID']
        is_pre = inst['PreAsset']
        epoch = inst['Epoch']
        nodekey = inst['NodeKey']
        rootchain_ip = inst['RootChain']["IpAddress"]
        res = change_account_operator(op_ip, op_key, op_addrs, op_pass, chain_id, is_pre, epoch, nodekey, rootchain_ip)
        t_db.update(set('IsSet', "true"), Query().InstanceId == inst_id)
        flash([time.ctime()[11:19] + " Operator Variable Set and signer.pass created"])
        return redirect(url_for('operator'))
    else:
        return redirect(url_for('operator'))

@app.route("/operator/deploy/rootchain", methods=["POST"])
def operator_deploy_rootchain():
    error = None
    res = []
    if request.method == 'POST':
        inst_id = request.form["instance_id"]
        inst = t_db.search(Query().InstanceId == inst_id)[0]
        inst_ip = inst['IpAddress']
        out1 = deploy_rootchain_contract(inst_ip)
        t_db.update(set('IsDeployed', "true"), Query().InstanceId == inst_id)
        flash([time.ctime()[11:19] + " rootchain contract deployed!"])
        return redirect(url_for('operator'))
    else:
        return redirect(url_for('operator'))

@app.route("/operator/export/genesis", methods=["POST"])
def operator_export_genesis():
    error = None
    res = []
    if request.method == 'POST':
        inst_id = request.form["instance_id"]
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
        inst_id = request.form["instance_id"]
        inst = t_db.search(Query().InstanceId == inst_id)[0]
        # TODO : initialize operator
        out = initialize_operator_blockchain(inst["IpAddress"])
        t_db.update(set('IsInitialized', "true"), Query().InstanceId == inst_id)
        flash([time.ctime()[11:19] + " Operator Initialized!"])
        return redirect(url_for('operator'))
    else:
        return redirect(url_for('operator'))

@app.route("/operator/runnode", methods=["POST"])
def operator_runnode():
    error = None
    res = []
    if request.method == 'POST':
        inst_id = request.form["instance_id"]
        inst = t_db.search(Query().InstanceId == inst_id)[0]
        out = run_operator(inst["IpAddress"])
        t_db.update(set('Status', "mining"), Query().InstanceId == inst_id)
        flash([time.ctime()[11:19] + " Operator Running!"])
        return redirect(url_for('operator'))
    else:
        return redirect(url_for('operator'))

@app.route("/operator/restart/<instanceid>")
def operator_restart(instanceid):
    inst = t_db.search(Query().InstanceId == instanceid)
    inst_ip = inst[0]["IpAddress"]

    restart_operator(inst_ip)

    flash([time.ctime()[11:19] + " Operator Restarted!"])
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

#######################
## USERNODE SETTING ###
#######################

@app.route("/usernode")
def usernode():
    data = t_db.search(Query().Type == "usernode")
    # print(data)
    return render_template(
            "usernode_list.html",
            data = data
        );

@app.route("/usernode/form")
def usernode_form():
    data = t_db.search(Query().Type == "rootchain")
    data2 = t_db.search(Query().Type == "operator")
    return render_template(
            "usernode_create_form.html",
            data = data,
            data2 = data2
        );

@app.route("/usernode/form/create", methods=["POST"])
def usernode_create():
    error = None
    res = []
    if request.method == 'POST':
        name = request.form['Name']
        rootchain_id = request.form['RootchainID']
        operator_id = request.form['OperatorID']
        enode_hex = request.form['enodehex']

        root_inst = t_db.search(Query().InstanceId == rootchain_id)[0]
        operator_inst = t_db.search(Query().InstanceId == operator_id)[0]

        # TODO : Create usernode
        # TODO : Create usernode monitor

        usernode_ins = create_usernode_instance(name)
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
                "Genesis" : operator_inst["Genesis"]
            },
            'InstanceId' : usernode_ins_monitor['InstanceMonitorings'][0]['InstanceId'],
            'Status' : usernode_ins_monitor['InstanceMonitorings'][0]['Monitoring']['State'],
            'Date' : usernode_ins_monitor['ResponseMetadata']['HTTPHeaders']['date'],
            'Enode' : enode_hex
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
        inst_id = request.form["instance_id"]
        user_inst = t_db.search(Query().InstanceId == inst_id)[0]

        #set variable
        user_ip = user_inst["IpAddress"]
        rootchain_ip = user_inst["RootChain"]["IpAddress"]
        operator_ip = user_inst["Operator"]["IpAddress"]
        enode_value = user_inst["Enode"]
        out1 = set_usernode_variable(user_ip, rootchain_ip, operator_ip, enode_value)
        print("out1 : ", out1)

        # import genesis to usernode
        genesis = user_inst["Operator"]["Genesis"]
        out2 = import_genesis_usernode(user_ip, genesis)
        check_genesis(user_ip)
        print("out1 : ", out2)

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
        inst_id = request.form["instance_id"]
        inst = t_db.search(Query().InstanceId == inst_id)[0]
        out = run_usernode(inst["IpAddress"])
        print(out)
        t_db.update(set('Status', "mining"), Query().InstanceId == inst_id)
        flash([time.ctime()[11:19] + " Usern Node Running!"])
        return redirect(url_for('usernode'))
    else:
        return redirect(url_for('usernode'))

#####################
## INSTANCE ROUTE ###
#####################

@app.route("/instance/<instanceid>")
def instance(instanceid):
    res = t_db.search(Query().InstanceId == instanceid)
    # print(instanceid)
    return render_template(
            "instance.html",
            data = res[0]
        );

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
        inst_id = request.form['instance_id']
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
        inst_id = request.form['instance_id']
        inst = t_db.search(Query().InstanceId == inst_id)[0]
        # TODO : CHECK STATUS - Pending | enable | mining | dead
        prior_status = t_db.search(Query().InstanceId == inst_id)[0]['Status']
        inst_resource = get_instance_resource(inst_id)
        inst_monitor = inst_resource.monitor()
        status = inst_monitor['InstanceMonitorings'][0]['Monitoring']['State']
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
        inst_id = request.form['instance_id']
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
        inst_id = request.form['instance_id']
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
