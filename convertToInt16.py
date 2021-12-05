import struct
import csv

pathWrite = ""
pathRead = ""
header = ["", "", "", "", "", "", "", "", "", ""]
data = []

try:
    with open(pathRead, "rb") as readFile:
        with open(pathWrite, "w") as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(header)
            bytes = readFile.read(20)
            while bytes:
                integers = struct.unpack('h' * 10, bytes)
                data.append(integers)
                bytes = readFile.read(20)
            writer.writerows(data)
except IOError:
    print('Error While Opening the file!')
