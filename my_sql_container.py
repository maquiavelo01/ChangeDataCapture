import os
import sys
import pymysql

# ----------------
# input arguments
# ----------------
# -delete, delete containers    
# -create, create containers
# -init, init mysql,

# delete containers
def delete(container):
    cmd = f'docker stop {container}'
    result = os.system(cmd)
    if (result == 0):
        cmd = f'docker rm {container}'
        result = os.system(cmd)
        print(f'Removed {container}')

# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')

# read input argument
argument = len(sys.argv)
if (argument > 1):    
    argument = sys.argv[1]     

# if -delete input argument, delete containers
if(argument == '-delete'):
    delete('final_mysql_container')
    sys.exit()

# if -create input argument, create containers
if(argument == '-create'):
    create('docker run -p 5600:3306 --name final_mysql_container -e MYSQL_ROOT_PASSWORD=MyNewPass -d mysql', 'mysql')
    sys.exit()


if(argument == '-init'):
    sys.exit()