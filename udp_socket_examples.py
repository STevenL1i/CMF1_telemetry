import socket

IP = "127.0.0.1"
PORT = 20888
SAVEFILEPATH = "./test_data/data_20241122_a2japan_testing.bin"

def write_bytedata_to_file(data:bytes, filepath:str=None):
    if filepath is None:
        filepath = SAVEFILEPATH
    with open(filepath, "ab") as f:
        f.write(data)
        f.write(b'\n')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))


while True:
    data, addr = sock.recvfrom(8192)
    print("received from: ", addr)
    print("received message: ", data)
    write_bytedata_to_file(data)
