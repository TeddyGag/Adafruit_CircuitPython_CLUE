from adafruit_clue import clue

clue.sea_level_pressure = 1020

while True:
    print("Acceleration: {:.2f} {:.2f} {:.2f}".format(*clue.acceleration))
    print("Gyro: {:.2f} {:.2f} {:.2f}".format(*clue.gyro))
    print("Magnetic: {:.3f} {:.3f} {:.3f}".format(*clue.magnetic))
    print("Pressure: {:.3f}hPa".format(clue.pressure))
    print("Altitude: {:.1f}m".format(clue.altitude))
    print("Temperature: {:.1f}C".format(clue.temperature))
    print("Humidity: {:.1f}%".format(clue.humidity))
    print("Proximity: {}".format(clue.proximity))
    print("Gesture: {}".format(clue.gesture))
    print("Color: R: {} G: {} B: {} C: {}".format(*clue.color))
    print("--------------------------------")
