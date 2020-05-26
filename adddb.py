import serial
import pymysql

ser = serial.Serial('COM6',9600)
DB = pymysql.connect(
    host='localhost',
    port = '80',
    user='user',
    password='1234',
    db='capston',
    charste='utf8'
)

db_curs = DB.cursor()
i = 0
while True:
    try:
        RMSCurrent = 0.0
        RMSPower = 0.0
        kilos = 0.0
        peakPower = 0.0
        ele = 0
        while True:
            # get data
            dataline = ser.readline()
            print(dataline.decode('ascii'))
            dataline = dataline.decode('ascii')

            if ('RMSCurrent' in dataline) and (ele == 0):
                RMSCurrent = dataline.split(":")[-1]
                RMSCurrent = float(RMSCurrent)
                ele += 1
            elif ('RMSPower' in dataline) and (ele == 1):
                RMSPower = dataline.split(":")[-1]
                RMSPower = float(RMSPower)
                ele +=1
            elif ('kilos' in dataline) and (ele == 2):
                kilos = dataline.split(":")[-1]
                kilos = float(kilos)
                ele += 1
            elif ('peakPower' in dataline) and (ele == 3):
                peakPower = dataline.split(":")[-1]
                peakPower = float(peakPower)
                ele += 1
            elif ('========' in dataline) and ( ele > 3):
                # save DB
                sql = "insert into info(RMSCurrent, RMSPower, kilos, peakPower) values (%f, %f, %f, %f)"
                db_curs.execute(sql, RMSCurrent, RMSPower, kilos, peakPower)
                print("OK : ", RMSCurrent, RMSPower, kilos, peakPower)
                DB.commit()
                break;
            else:
                printf("something wrong : ", ele) # remove all []
                break;

    except KeyboardInterrupt:
        print("U close program by key interrupt (Ctrl + C)")
        exit(1)
print("Program ended")
