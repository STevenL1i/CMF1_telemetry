import sys
import struct


f = open("./test_data/data_20241121_testing.bin", 'rb')

data = f.read()

f.close()


data_list = data.split(b'\n')
for data in data_list:
    print(data)

