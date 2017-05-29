from st2actions.runners.pythonrunner import Action
from ssh_access import ssh_session
import os.path
import re

class onlineport(Action):

        def run(self, ip_address, username, password, enable_username, enable_password, device_ip_address, vrf="default-vrf"):
            print "started processing..."
            h1 = ssh_session(ip_address, username, password, enable_username, enable_password, 'ping '+device_ip_address+" vrf "+vrf)
            h1.ssh_access()
            file_path = os.path.relpath("/tmp/sshoutputlog.txt")
            infile = open(file_path,"r")
            connection = False
            for line in infile:
                match = re.search("bytes from", line)
                if match:
                    connection = True

            return (connection)
            infile.close()

