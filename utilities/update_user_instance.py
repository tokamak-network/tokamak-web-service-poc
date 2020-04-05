from utilities import SSHManager
import subprocess

"""
usage:
    >>> import SSHManager
    >>> ssh_manager = SSHManager()
    >>> ssh_manager.create_ssh_client(hostname, username, password, pemfile)
    >>> ssh_manager.send_command("ls -al")
    >>> ssh_manager.send_file("/path/to/local_path", "/path/to/remote_path")
    >>> ssh_manager.get_file("/path/to/remote_path", "/path/to/local_path")
    ...
    >>> ssh_manager.close_ssh_client()
"""

if __name__ == "__main__":
    ##### update before use it #####
    hostname = "52.194.187.153"
    username = "ubuntu"
    pemfile = "../test_kevin1.pem"

    ssh_manager = SSHManager()
    ssh_manager.create_ssh_client(hostname, username, pemfile)

    # 1. zip local scripts/rootchain directory
    subprocess.call(["tar","cvf","user.scripts.tar","-C","../scripts/usernode","."])

    # 2. transport file
    ssh_manager.send_file("user.scripts.tar", "/home/ubuntu/")

    # 3. unzip
    ssh_manager.send_command("tar xvf user.scripts.tar -C ./")

    # 4. stop all geth
    ssh_manager.send_command("./reset.sh")

    # TODO : git pull plasma-evm and make
    # TODO : make aws instance AMI and print it

    ssh_manager.close_ssh_client()
