def logRun(acc,mp,mpp,si,lt)

    T_AMBIENT = 24.4
    runAcc = []
    runRoll = []
    runPitch = []
    height = []
    temperature = []
    pressure = []
    battV = []
    humidity = []
    ambHumidity = []
    dewPoint = []

    acc.enable_activity_interrupt(2000, 200) #run while acceleration is greater than 2G for 200 ms
    while acc.activity():
        runAcc.append(acc.acceleration())
        runRoll.append(acc.roll())
        runPitch.append(acc.pitch())
        height.append(mp.altitude())
        temperature.append((mp.temperature()+si.temperature())/2) #Average both temperature values
        pressure.append(mpp.pressure())
        battV.append(py.read_battery_voltage())
        humidity.append(si.humidity())
        ambHumidity.append(si.humid_ambient(T_AMBIENT))
        dewPoint.append(si.dew_point())
        time.sleep(0.05)
    
