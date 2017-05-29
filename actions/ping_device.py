name: "onlineport"
runner_type: "python-script"
description: "is the port online or not?"
enabled: true
entry_point: "onlineport.py"
parameters:
  ip_address:
    type: "string"
    description: "ip address of the switch"
    required: true
  username:
    type: "string"
    description: "Login Username"
    required: true
  password:
    type: "string"
    description: "Login Password"
    required: true
  enable_username:
    type: "string"
    description: "Enable Username"
    required: true
  enable_password:
    type: "string"
    description: "Enable Password"
    required: true
  port:
    type: "string"
    description: "Port x/y/z"
    required: true

