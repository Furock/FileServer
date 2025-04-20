#server.py must lay in the same directory as fileserver.sh
python $(dirname ${BASH_SOURCE[0]})/server.py

#alternatively put this path to your path var and use:
#python $(where server.py)