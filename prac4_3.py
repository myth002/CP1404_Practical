#Pgm to detect authentication of usernames

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

u=str(input("Enter your username: "))
if u in usernames:
    print("Access Granted")
else:
    print("Access Denied")