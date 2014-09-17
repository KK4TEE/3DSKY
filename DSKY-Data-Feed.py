#DSKY-Data-Feed
'''This is a complete rewrite of my previous Flight Terminal program.
This is designed to work with the 3d printed DSKY replica, but it should work
with any sort of similar program.'''
import math
import time
import config
import telemachus_plugin as tele
import telemachus_plugin

try:
    import serial
except:
    print 'PySerial does not seem to be installed'

try:
    ser = serial.Serial(
        port=config.arduinoSerialPort(),
        #port='COM3',
        #baudrate=115200, # Causes the arduino buffer to fill up
        #baudrate=28800, #doesn't seem to work at all
        baudrate=9600,  # Seems to be working well
       # parity=serial.PARITY_ODD,
       # stopbits=serial.STOPBITS_TWO,
       # bytesize=serial.SEVENBITS
    )
    arduinoConnected = True
    print 'Serial device connected at ' + config.arduinoSerialPort()
except:
    arduinoConnected = False
    print 'Unable to connect to arduino at ' + config.arduinoSerialPort()
print 'Waiting 3 for Arduino to boot...'
time.sleep(3)

def getFlightData(dIN):
    # Try to update the dictionary with live data. If any of it fails for any
    # reason, return the original dictionary and set the 'Radio Contact' key
    # to false.
    d = {'Zero': 0}
    try:
        d['MET'] = float(tele.read_missiontime())
        d['ASL'] = int(tele.read_asl())
        d['Height From Terrain'] = int(tele.read_heightFromTerrain())
        d['Body'] = str(tele.read_body())
        d['Ap'] = int(tele.read_apoapsis())
        d['Pe'] = int(tele.read_periapsis())
        d['Time to Ap'] = float(tele.read_time_to_ap())
        d['Time to Pe'] = float(tele.read_time_to_pe())
        d['Eccentricity'] = float(tele.read_eccentricity())
        d['Inclination'] = float(tele.read_inclination())
        d['Orbital Period'] = float(tele.read_orbitalperiod())
        d['Vertical Speed'] = float(tele.read_verticalspeed())
        d['Surface Speed'] = float(tele.read_surfacespeed())
        d['Pitch'] = float(tele.read_facing('pitch'))
        d['Yaw'] = float(tele.read_facing('yaw'))
        d['Roll'] = float(tele.read_facing('roll'))
        d['Throttle'] = float(tele.read_throttle())

        d['Brake Status'] = int(tele.brake(2))
        d['Gear Status'] = int(tele.gear(2))
        d['SAS Status'] = int(tele.sas(2))
        d['RCS Status'] = int(tele.rcs(2))
        d['Light Status'] = int(tele.light(2))

        d['ElectricCharge'] = float(tele.read_resource('ElectricCharge'))
        d['Max ElectricCharge'] = float(tele.read_resource_max(
            'ElectricCharge'))
        d['LiquidFuel'] = float(tele.read_resource('LiquidFuel'))
        d['Max LiquidFuel'] = float(tele.read_resource_max('LiquidFuel'))
        d['Oxidizer'] = float(tele.read_resource('Oxidizer'))
        d['Max Oxidizer'] = float(tele.read_resource_max('Oxidizer'))
        d['SolidFuel'] = float(tele.read_resource('SolidFuel'))
        d['Max SolidFuel'] = float(tele.read_resource_max('SolidFuel'))
        d['MonoPropellant'] = float(tele.read_resource('MonoPropellant'))
        d['Max MonoPropellant'] = float(tele.read_resource_max('MonoPropellant'))
        # If you are playing with realism mods, uncomment these as needed
        #d['Oxygen'] = float(tele.read_resource('Oxygen'))
        #d['Max Oxygen'] = float(tele.read_resource_max('Oxygen'))
        #d['LiquidOxygen'] = float(tele.read_resource('LiquidOxygen'))
        #d['Max LiquidOxygen'] = float(tele.read_resource_max('LiquidOxygen'))
        #d['LiquidH2'] = float(tele.read_resource('LiquidH2'))
        #d['Max LiquidH2'] = float(tele.read_resource_max('LiquidH2'))
        #d['MMH'] = float(tele.read_resource('MMH'))
        #d['Max MMH'] = float(tele.read_resource_max('MMH'))
        #d['N2O4'] = float(tele.read_resource('N2O4'))
        #d['Max N2O4'] = float(tele.read_resource_max('N2O4'))

        d['Previous Radio Contact'] = dIN['Radio Contact']
        d['Radio Contact'] = True

        #Clean up the data types
        if d['SAS Status'] == 1:
            d['SAS Status'] = True
        elif d['SAS Status'] == 0:
            d['SAS Status'] = False
        else:
            d['SAS Status'] = 'Error'
        if d['RCS Status'] == 1:
            d['RCS Status'] = True
        else:
            d['RCS Status'] = False
        if d['Light Status'] == 1:
            d['Light Status'] = True
        else:
            d['Light Status'] = False
        if d['Gear Status'] == 1:
            d['Gear Status'] = True
        elif d['Gear Status'] == 0:
            d['Gear Status'] = False
        if d['Brake Status'] == 1:
            d['Brake Status'] = True
        elif d['Brake Status'] == 0:
            d['Brake Status'] = False

        print "Flight data updated."
        return d


    except:
        dIN['Previous Radio Contact'] = dIN['Radio Contact']
        dIN['Radio Contact'] = False
	print "An error occured while requesting flight data"
        del d
        return dIN


def buttonHandler():
    # Reads memB for which buttons are pressed, then sends
    # calls to telemachus as needed.
    global memB
    global memBOLD
    if memB[1] == '1' and memB[1] != memBOLD[1]:
        if (memB[7] == '1'):  # Check the safety
            tele.stage()

    if memB[0] == '1' and memB[0] != memBOLD[0]:
        if memB[7] == '1':  # Check the safety
            tele.abort()

    if int(memB[2]) == 1 and memB[2] != memBOLD[2]:
        # Toggle gear based on what we did last time
        if ps['Gear Status'] is True:
            # Telemachus does not yet read gear status
            tele.gear(0)
            ps['Gear Status'] = False
        elif ps['Gear Status'] is False:
            tele.gear(1)
            ps['Gear Status'] = True

    if int(memB[3]) == 1 and memB[3] != memBOLD[3]:
        # Toggle Light based on the Telemachus reading
        if fd['Light Status'] is True:
            tele.light(0)
        elif fd['Light Status'] is False:
            tele.light(1)

    if int(memB[4]) == 1 and memB[4] != memBOLD[4]:
        # Toggle brake based on what we did last time
        if ps['Brake Status'] is True:
            # Telemachus does not yet read brake status
            tele.brake(0)
            ps['Brake Status'] = False
        elif ps['Brake Status'] is False:
            tele.brake(1)
            ps['Brake Status'] = True

    if int(memB[5]) == 1 and memB[5] != memBOLD[5]:
        # Toggle RCS based on the Telemachus reading
        if fd['RCS Status'] is True:
            tele.rcs(0)
        elif fd['RCS Status'] is False:
            tele.rcs(1)

    if int(memB[6]) == 1 and memB[6] != memBOLD[6]:
        # Toggle SAS based on the Telemachus reading
        if fd['SAS Status'] is True:
            tele.sas(0)
        elif fd['SAS Status'] is False:
            tele.sas(1)


def push_to_arduino(inputline):
    #Packet Size: 38 Bytes
    #Header "<"
    #memA[0] Program Select
    #memA[1] Red LEDs [Alarm, SAS, RCS, Gear, Brake, Case/Body*, Keyboard Backlight*]
    #memA[2] Green LEDs [Alarm, SAS, RCS, Gear, Brake, Case/Body*, Keyboard Backlight*]
    #memA[3] Not Used
    #memA[4-36] 7 Segment Display Digits, starting in the top left corner
    #Footer ">"

    # Send data to inside of a header and footer
    if len(inputline) is 36:
        ser.write('<' + inputline + '>')
	print("Transmitting: " + '<' + inputline + '>')
    else:
        print 'Error: An amount other than 36 characters was passed to push_to_arduino'


def formatForArduino(mode):
    #Packet Size: 38 Bytes
    #Header "<"
    #memA[0] Program Select
    #memA[1] Red LEDs [Alarm, SAS, RCS, Gear, Brake, Case/Body*, Keyboard Backlight*]
    #memA[2] Green LEDs [Alarm, SAS, RCS, Gear, Brake, Case/Body*, Keyboard Backlight*]
    #memA[3] Not Used
    #memA[4-36] 7 Segment Display Digits, starting in the top left corner
    #Footer ">"

    if mode == 'Lamp Test':  # Light Test
        arduino['7r0 Data'] = '88888888'
        arduino['7r1 Data'] = '88888888'
        arduino['7r2 Data'] = '88888888'
        arduino['7r3 Data'] = '88888888'
        arduino['7r4 Data'] = '88888888'


    elif mode == 'Clock':
        '''There's something weird going on here that causes the code to
        take a full 300ms or so to loop. This requires further research.'''
        arduino['7r0 Data'] = '        '
        arduino['7r1 Data'] = str(time.strftime("%H %M %S"))
        arduino['7r2 Data'] = str(time.strftime(" %m  %d "))
        arduino['7r3 Data'] = str(time.strftime("  %Y  "))
        arduino['7r4 Data'] = '        '

    else:
        arduino['7r0 Data'] = str(int(round(fd["Time to Ap"]))).zfill(8)
        arduino['7r1 Data'] = str(int(round(fd["ASL"] / 100))).zfill(8)
        arduino['7r2 Data'] = str(int(round(fd["Ap"] / 100))).zfill(8)
        arduino['7r3 Data'] = str(int(round(fd["Pe"] / 100))).zfill(8)
        arduino['7r4 Data'] = str(int(round(fd["MET"]))).zfill(8)
	arduino['LEDG'] = 0
	if fd['Throttle'] > 0:
            arduino['LEDG'] += 1<<0
        if fd['SAS Status'] is True:
            arduino['LEDG'] += 1<<1
        if fd['RCS Status'] is True:
            arduino['LEDG'] += 1<<2
        if fd['Gear Status'] is True:
            arduino['LEDG'] += 1<<3
        if fd['Brake Status'] is True:
            arduino['LEDG'] += 1<<4
	if arduino['Backlight'] is True:
            arduino['LEDG'] += 1<<5
	print bin(arduino['LEDG'])
	arduino['LEDG'] = chr(arduino['LEDG'])

	arduino['LEDR'] = 0
	if fd['ElectricCharge'] < (fd['Max ElectricCharge'] / 10):
            arduino['LEDR'] += 1<<0
        if fd['SAS Status'] is False:
            arduino['LEDR'] += 1<<1
        if fd['RCS Status'] is False:
            arduino['LEDR'] += 1<<2
        if fd['Gear Status'] is False:
            arduino['LEDR'] += 1<<3
        if fd['Brake Status'] is False:
            arduino['LEDR'] += 1<<4
	print bin(arduino['LEDR'])
	arduino['LEDR'] = chr(arduino['LEDR'])



def clamp(num, minn, maxn):
    if num < minn:
        return minn
    elif num > maxn:
        return maxn
    else:
        return num


######################################################################################

# Flight Data Memory and other variables
fd = {  # Primary data storage
'MET': -1, 'ASL': -1, 'Ap': -1, 'Pe': -1, 'Time to Ap': -1, 'Time to Pe': -1,
'Eccentricity': -1, 'Inclination': -1, 'Orbital Period': -1,
'Vertical Speed': -1, 'Surface Speed': -1, 'Pitch': -1, 'Roll': -1, 'Yaw': -1,
'Height From Terrain': -1,
'Throttle': -1, 'SAS Status': -1, 'RCS Status': -1, 'Light Status': -1,
'Brake Status': -1, 'Gear Status': -1,
'ElectricCharge': -1, 'Max ElectricCharge': -1,
'LiquidFuel': -1, 'Max LiquidFuel': -1,
'Oxidizer': -1, 'Max Oxidizer': -1,
'SolidFuel': -1, 'Max SolidFuel': -1,
'MonoPropellant': -1, 'Max MonoPropellant': -1,
'Oxygen': -1, 'Max Oxygen': -1,  # Realisim Resources
'LiquidH2': -1, 'Max LiquidH2': -1,
'LiquidOxygen': -1, 'Max LiquidOxygen': -1,
'MMH': -1, 'Max MMH': -1,
'N2O4': -1, 'Max N2O4': -1,
'Radio Contact': False, 'Previous Radio Contact': False}

ps = {  # Program Settings
'Main Menu is Open': False, 'Main Menu Selection': 1, 'Slection Made': False,
'Display Mode': 'Standard',
'Flight Transceiver Active': True,
'Terminal Max Y': 25, 'Terminal Max X': 40,
'Arduino Sleep Marker': 0, 'Arduino Active': False, 'Button Sleep Marker': 0,
'flightData Sleep Marker': 0, 'Gear Status': False, 'Brake Status': False}

arduino = {  # Arduino Configurtion, using rows
'Program': str('Z'),
'LEDR': str('z'),
'LEDG': str('z'),
'Byte3': str('z'),
'7r0 Name': 'MET', '7r0 Data': str().zfill(8),
'7r1 Name': 'ASL', '7r1 Data': str().zfill(8),
'7r2 Name': 'Ap', '7r2 Data': str().zfill(8),
'7r3 Name': 'Pe', '7r3 Data': str().zfill(8),
'7r4 Name': 'Time to Ap', '7r4 Data': str().zfill(8),
'g0 Name': 'MET', 'g0 Data': str().zfill(1),
'Backlight': True
}

arduinoSleepMarker = 0
buttonSleepMarker = 0
flightDataSleepMarker = config.pollInterval()
memB = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Current serial input
memBOLD = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Old serial input

###############################################################################################
while True:
    loopStartTime = time.time()
    fd = getFlightData(fd)
    if arduinoConnected is True:
        formatForArduino('Telemetry')
        memA = (
            str(arduino['Program']) +
            str(arduino['LEDR']) +
            str(arduino['LEDG']) +
            str(arduino['Byte3']) +
            str(arduino['7r0 Data']) +
            str(arduino['7r1 Data']) +
            str(arduino['7r2 Data']) +
            str(arduino['7r3 Data'])

            )

        if arduinoSleepMarker > 0.10:
            try:
                push_to_arduino(memA)
            except:
                print "Error pushing to Arduino"
                pass
            finally:
                arduinoSleepMarker = 0
        '''
        if ser.inWaiting > 9:
            try:
                serCharIn = str(ser.read(1))
                if serCharIn == '<':
                    while n < 12:
                        serCharIn = str(ser.read(1))
                        if serCharIn == '>':
                            n = 0
                            ser.flushInput()
                            break
                        else:
                            memB[n] = serCharIn
                        n += 1
                        if n == 11:
                            ser.flushInput()
            except:
                ser.flushInput()'''
        ser.flushInput()
        if buttonSleepMarker > 0.1:
            buttonHandler()
            button_sleep_marker = 0
            memBOLD = list(memB)

    loopTimeOffset = config.pollInterval() + loopStartTime - time.time()
        # This can be used to slow the entire program down to cycle at a
        # given interval. This is a failsafe to prevent 100% utilization
    if loopTimeOffset > 0:
        time.sleep(loopTimeOffset)
    # Combined Bandwidth used based on interval:
    # 33ms = around 395 Packets/S, 345kbs
    # 25ms = around 500 Packets/S, 410kbs
    loopEndTime = time.time()
    loopTime = loopEndTime - loopStartTime
    arduinoSleepMarker += loopTime
    buttonSleepMarker += loopTime
    flightDataSleepMarker += loopTime

