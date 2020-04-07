from .utilities import SSHManager
import subprocess

def update_operator(hostname, username, pemfile):
    ssh_manager = SSHManager()
    ssh_manager.create_ssh_client(hostname, username, pemfile)

    # 1. zip local scripts/rootchain directory
    subprocess.call(["tar","cvf","oper.scripts.tar","-C","scripts/operator","."])

    # 2. transport file
    ssh_manager.send_file("oper.scripts.tar", "/home/ubuntu/")

    # 3. unzip
    ssh_manager.send_command("tar xvf oper.scripts.tar -C ./")

    # 4. stop all geth
    ssh_manager.send_command("./initialize.sh")

    # TODO : git pull plasma-evm and make
    # TODO : make aws instance AMI and print it

    ssh_manager.close_ssh_client()

def update_rootchain(hostname, username, pemfile):
    # hostname = "3.112.188.20"
    # username = "ubuntu"
    # pemfile = "../test_kevin1.pem"

    ssh_manager = SSHManager()
    ssh_manager.create_ssh_client(hostname, username, pemfile)

    # 1. zip local scripts/rootchain directory
    subprocess.call(["tar","cvf","rootchain.scripts.tar","-C","scripts/rootchain","."])

    # 2. transport file
    ssh_manager.send_file("rootchain.scripts.tar", "/home/ubuntu/")

    # 3. unzip
    ssh_manager.send_command("tar xvf rootchain.scripts.tar -C ./")

    # 4. stop all geth
    ssh_manager.send_command("./reset.rootchain.sh")

    # TODO : git pull go-ethereum and make
    # TODO : git pull plasma-evm and make
    # TODO : make aws instance AMI and print it

    ssh_manager.close_ssh_client()

def update_usernode(hostname, username, pemfile):
    # hostname = "52.194.187.153"
    # username = "ubuntu"
    # pemfile = "../test_kevin1.pem"

    ssh_manager = SSHManager()
    ssh_manager.create_ssh_client(hostname, username, pemfile)

    # 1. zip local scripts/rootchain directory
    subprocess.call(["tar","cvf","user.scripts.tar","-C","scripts/usernode","."])

    # 2. transport file
    ssh_manager.send_file("user.scripts.tar", "/home/ubuntu/")

    # 3. unzip
    ssh_manager.send_command("tar xvf user.scripts.tar -C ./")

    # 4. stop all geth
    ssh_manager.send_command("./reset.sh")

    # TODO : git pull plasma-evm and make
    # TODO : make aws instance AMI and print it

    ssh_manager.close_ssh_client()
