import os

def run_system_command(cmd):
    os.system(cmd)

count=input()

for i in range(int(count)):
    cmd=input()
    run_system_command(cmd)
