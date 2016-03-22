import paramiko
import sys
hostname=str(sys.argv[1])
username=str(sys.argv[2])
id_rsa_file_path=str(sys.argv[3])
#key = paramiko.from_private_key_file("~/.ssh/id_rsa")
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname,username=username,key_filename=id_rsa_file_path)
stdin,stdout,stderr=ssh.exec_command('free -m')
for lines in stdout:
    print(lines,end='')
ssh.close()