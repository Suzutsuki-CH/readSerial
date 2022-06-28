import serial

port = "/COM5"
baud = 115200  # accelerometer output at 115200 baud
fileName = "AGM_data.csv"
sample = 20
printLabels = False

ser = serial.Serial(port, baud)
# print("Connected to port: " + port)
file = open(fileName, "a")
# print("File created")
while True:
    AGMdata = ser.readline()
    print(AGMdata)

line = 0


