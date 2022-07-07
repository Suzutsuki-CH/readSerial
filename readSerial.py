import serial


port = "/COM5"
baud = 115200  # accelerometer output at 115200 baud
fileName = "AGM_data.csv"
sample = 2000
printLabels = False

ser = serial.Serial(port, baud)
# print("Connected to port: " + port)
file = open(fileName, "a")
# print("File created")

line = 0

#while True:
    # AGMdata = ser.readline()
    # print(str(AGMdata)[2:-5])

AGMdata = ser.readline()

while line < sample:
    AGMdata = ser.readline()
    file = open("AGM_data.csv","a")

    file.write(str(AGMdata)[2:-5] + "\n")

    line += 1



