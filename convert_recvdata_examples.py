import sys
import struct
#data = b'\xe8\x07\x18\x01\x0e\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00BUTN@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
data = b"\xe8\x07\x18\x01\x0e\x01\x019\x99u\x91\x9d\x02\x9b\x14\x1d\xdd\x0eB\xcd\x02\x00\x00\xcd\x02\x00\x00\x00\xff\x00-\x1e\x01 \x15\x12\x03\x00\x00\x00X\x02P\x00\x00\xff\x00\x11\xb1Lt?\x00XG\xdc=\x00\xfd\xe00>\x00z\xee\x81>\x00p'\xa4>\x00fo\xb4>\x00H\x9a\xc1>\x00\xbf\xfb\xd2>\x00\x83\x01\xe4>\x00\xee\x84\xf7>\x00\rf\x03?\x00\xe34 ?\x00\x81=)?\x00P\x8f1?\x00\x83\x01@?\x00\x03iM?\x00^\xfdc?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x05\x02\xdc\x02\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x01\x01\x03\x01\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x01\x01\x02\x00\xff\x00\xff\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa9\x93\xe1D\xc6`zE"


cursor = 0


header_dict = dict()
########################################### analysis header ###########################################
packetformat_byte = data[cursor:cursor+2]
# packetformat = struct.unpack('<H', packetformat_byte)[0]
packetformat = int.from_bytes(packetformat_byte, 'little')
header_dict["Format"] = {"data": packetformat, "bytes": packetformat_byte}
cursor += 2

gameyear_byte = data[cursor:cursor+1]
#gameyear = struct.unpack('<B', gameyear_byte)[0]
gameyear = int.from_bytes(gameyear_byte, 'little')
header_dict["Game Year"] = {"data": gameyear, "bytes": gameyear_byte}
cursor += 1

gameMajorVersion_byte = data[cursor:cursor+1]
#gameMajorVersion = struct.unpack('<B', gameMajorVersion_byte)[0]
gameMajorVersion = int.from_bytes(gameMajorVersion_byte, 'little')
header_dict["Major Ver."] = {"data": gameMajorVersion, "bytes": gameMajorVersion_byte}
cursor += 1

gameMinorVersion_byte = data[cursor:cursor+1]
#gameMinorVersion = struct.unpack('<B', gameMinorVersion_byte)[0]
gameMinorVersion = int.from_bytes(gameMinorVersion_byte, 'little')
header_dict["Minor Ver."] = {"data": gameMinorVersion, "bytes": gameMinorVersion_byte}
cursor += 1

packetVersion_byte = data[cursor:cursor+1]
#packetVersion = struct.unpack('<B', packetVersion_byte)[0]
packetVersion = int.from_bytes(packetVersion_byte, 'little')
header_dict["Packet Ver."] = {"data": packetVersion, "bytes": packetVersion_byte}
cursor += 1

packetID_byte = data[cursor:cursor+1]
#packetID = struct.unpack('<B', packetID_byte)[0]
packetID = int.from_bytes(packetID_byte, 'little')
header_dict["Packet ID"] = {"data": packetID, "bytes": packetID_byte}
cursor += 1

sessionUID_byte = data[cursor:cursor+8]
sessionUID = struct.unpack('<LL', sessionUID_byte)[0]
#sessionUID = int.from_bytes(sessionUID_byte, 'little')
header_dict["sessionUID"] = {"data": sessionUID, "bytes": sessionUID_byte}
cursor += 8

sessionTime_byte = data[cursor:cursor+4]
sessionTime = struct.unpack('<f', sessionTime_byte)[0]
# sessionTime = int.from_bytes(sessionTime_byte, 'little')
header_dict["sessionTime"] = {"data": sessionTime, "bytes": sessionTime_byte}
cursor += 4

frameID_byte = data[cursor:cursor+4]
frameID = int.from_bytes(frameID_byte, 'little')
header_dict["frameID"] = {"data": frameID, "bytes": frameID_byte}
cursor += 4

overallframeID_byte = data[cursor:cursor+4]
overallframeID = int.from_bytes(overallframeID_byte, 'little')
header_dict["overallframeID"] = {"data": overallframeID, "bytes": overallframeID_byte}
cursor += 4

playerCarIndex_byte = data[cursor:cursor+1]
playerCarIndex = int.from_bytes(playerCarIndex_byte, 'little')
header_dict["playerCarIndex"] = {"data": playerCarIndex, "bytes": playerCarIndex_byte}
cursor += 1

secondCarIndex_byte = data[cursor:cursor+1]
secondCarIndex = int.from_bytes(secondCarIndex_byte, 'little')
header_dict["secondCarIndex"] = {"data": secondCarIndex, "bytes": secondCarIndex_byte}
cursor += 1


1484783377922234681


session_dict = dict()
########################################### analysis session ###########################################
weather_byte = data[cursor:cursor+1]
weather = int.from_bytes(weather_byte, 'little')
session_dict["weather"] = {"data": weather, "bytes": weather_byte}
cursor += 1

trackTemp_byte = data[cursor:cursor+1]
trackTemp = int.from_bytes(trackTemp_byte, 'little')
session_dict["trackTemp"] = {"data": trackTemp, "bytes": trackTemp_byte}
cursor += 1

airTemp_byte = data[cursor:cursor+1]
airTemp = int.from_bytes(airTemp_byte, 'little')
session_dict["airTemp"] = {"data": airTemp, "bytes": airTemp_byte}
cursor += 1

totalLaps_byte = data[cursor:cursor+1]
totalLaps = int.from_bytes(totalLaps_byte, 'little')
session_dict["totalLaps"] = {"data": totalLaps, "bytes": totalLaps_byte}
cursor += 1

trackLength_byte = data[cursor:cursor+2]
trackLength = int.from_bytes(trackLength_byte, 'little')
session_dict["trackLength"] = {"data": trackLength, "bytes": trackLength_byte}
cursor += 2

sessionType_byte = data[cursor:cursor+1]
sessionType = int.from_bytes(sessionType_byte, 'little')
session_dict["sessionType"] = {"data": sessionType, "bytes": sessionType_byte}
cursor += 1

trackID_byte = data[cursor:cursor+1]
trackID = int.from_bytes(trackID_byte, 'little')
session_dict["trackID"] = {"data": trackID, "bytes": trackID_byte}
cursor += 1

formula_byte = data[cursor:cursor+1]
formula = int.from_bytes(formula_byte, 'little')
session_dict["formula"] = {"data": formula, "bytes": formula_byte}
cursor += 1







# print data
col1, col2, col3 = 40, 30, 10
for k in header_dict.keys():
    print(f'{k:<{col1}}{header_dict[k]["data"]:<{col2}}{header_dict[k]["bytes"]}')
print("\n\n")
for k in session_dict.keys():
    print(f'{k:<{col1}}{session_dict[k]["data"]:<{col2}}{session_dict[k]["bytes"]}')



'''
print(f'{"Format":<{col1}}{packetformat:<{col2}}{packetformat_byte}')
print(f'{"Game Year":<{col1}}{gameyear:<{col2}}{gameyear_byte}')
print(f'{"Major Ver.":<{col1}}{gameMajorVersion:<{col2}}{gameMajorVersion_byte}')
print(f'{"Minor Ver.":<{col1}}{gameMinorVersion:<{col2}}{gameMinorVersion_byte}')
print(f'{"Packet Ver.":<{col1}}{packetVersion:<{col2}}{packetVersion_byte}')
print(f'{"Packet ID":<{col1}}{packetID:<{col2}}{packetID_byte}')
'''
