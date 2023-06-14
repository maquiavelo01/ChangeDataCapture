import os
import sys
from cassandra.cluster import Cluster

# ----------------
# input arguments
# ----------------
# -delete, delete containers    
# -create, create containers
# -init, init 

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
    delete('final_cassandra_container')
    sys.exit()

# if -create input argument, create containers
if(argument == '-create'):
    create('docker run -p 1000:9042 --name final_cassandra_container -d cassandra', 'cassandra')
    sys.exit()

# if -init, init mysql
if(argument == '-init'):
    sys.exit()