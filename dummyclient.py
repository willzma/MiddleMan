from socketIO_client import SocketIO

messages_outstanding = 0

def emit(socket_instance, endpoint, payload):
    global messages_outstanding
    def callback(*args):
        global messages_outstanding
        messages_outstanding -= 1
    messages_outstanding += 1
    socketIO.emit(endpoint, payload, callback)
    socketIO.wait_for_callbacks(seconds=1)

def terminate(socket_instance):
    global messages_outstanding
    while messages_outstanding > 0:
        print("Awaiting " + str(messages_outstanding) + " callbacks.")
    socket_instance.disconnect()


with SocketIO('localhost', 8080) as socketIO:
    for i in range(1, 8):
        emit(socketIO, "", "SKUKTHEDUKUP"*(10**(i)))
        print("hey")
    terminate(socketIO)