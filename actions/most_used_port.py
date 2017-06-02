from st2actions.runners.pythonrunner import Action
from ssh_access import ssh_session
import os.path
import re

class most_used_port(Action):

        def run(self, ip_address, username, password, enable_username, enable_password):
            print "started processing..."
            h1 = ssh_session(ip_address, username, password, enable_username, enable_password, 'show interface stats detail')
            h1.ssh_access()
            file_path = os.path.relpath("/tmp/sshoutputlog.txt")
            infile = open(file_path,"r")
            interface = ""
            interface_max = ""
            rx_util = 0
            rx_util_max = 0
            tx_util = 0
            tx_util_max = 0
            for line in infile:
                match = re.search("Interface", line)
                if match:
                    interface = line.split( )[2]
                match = re.search("Line-rate", line)
                if match:
                    rx_util = float(line.split( )[1][0:4])
                    tx_util = float(line.split( )[2][0:4])
                    if (rx_util > rx_util_max) or (tx_util > tx_util_max):
                        interface_max = interface
                        rx_util_max = rx_util
                        tx_util_max = tx_util
            infile.close()
            if interface_max <> "":
                print "Most utilized Interface:",interface_max,"RX:",rx_util_max,"TX:",tx_util_max
                return (True, interface_max, rx_util_max, tx_util_max)
            else:
                return (False, "", 0.0, 0.0)
