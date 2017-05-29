import pexpect

class ssh_session(object):
        def __init__(self, ip_address, username, password, enable_username, enable_password, command):
                self.ip_address = ip_address
                self.username = username
                self.password = password
                self.enable_username = enable_username
                self.enable_password = enable_password
                self.command = command

        def ssh_access(self):
                """Secure Shell Access to a device"""
                ssh_login = "ssh %s@%s" % (self.username, self.ip_address)
                child = pexpect.spawn(ssh_login)
                i = child.expect(['timed out', 'assword', 'yes/no', 'failed', pexpect.TIMEOUT], timeout=30)
                if i == 1:
                    child.sendline(self.password)
                if i == 2:
                    child.sendline('yes')
                    child.expect("assword")
                    child.sendline(self.password)
                child.sendline('enable')
                child.expect("#")
                child.sendline('terminal length 0')
                child.expect("#")
                child.sendline(self.command)
                child.logfile = open("/tmp/sshoutputlog.txt", "w")
                child.expect("#")
                print child.before
                child.sendline('exit')
                child.close()

