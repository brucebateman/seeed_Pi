import grovepi
 
# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# SIG,NC,VCC,GND
sensor = 4
 
while True:
    try:
        [temp,humidity] = grovepi.dht(sensor,1)
        print "temp =", temp, " humidity =", humidity
 
    except IOError:
        print "Error"
