print("Module is running")

def mi2ft():
    usermiles = (input("Enter distance in miles you want converted to feet: "))
    userdist = float(usermiles)
    return(userdist * 5280)

def ft2mi():
    userfeet = (input("Enter distance in feet you want converted to miles: "))
    userdist = float(userfeet)
    return(userdist / 5280)

def c2f():
    usertemp = (input("Enter the temperature you want converted to degrees farenheit: "))
    temp = float(usertemp)
    return((temp * 1.8) + 32)

def f2c():
    usertemp = (input("Enter the temperature you want converted to degrees celcius: "))
    temp = float(usertemp)
    return((temp - 32) / 1.8)

def sec2hr():
    usertime = (input("Enter the time in seconds you want converted to hours: "))
    time = float(usertime)
    return(time / 3600)

def hr2sec():
    usertime = (input("Enter the time in hours you want converted to seconds: "))
    time = float(usertime)
    return(time * 3600)

def coord():

    mylist1 = []
    var1, var2 = [str(x) for x in input("Enter coordinates here: ").split(",")]
    dms_lat = var1
    dms_long = var2

    dms_lat = dms_lat.replace("°", ",").replace("\'", ",").replace("\"", ",").replace(" ", "")
    dms_long = dms_long.replace("°", ",").replace("\'", ",").replace("\"", ",").replace(" ", "")

    mylist1.append(dms_lat)
    mylist1.append(dms_long)

    mylist2 = []

    for item in mylist1:
        sub_items = item.split(",")
        mylist2.extend(sub_items)

    degrees_lat = float(mylist2[0])
    minutes_lat = float(mylist2[1])
    seconds_lat = float(mylist2[2])
    degrees_long = float(mylist2[4])
    minutes_long = float(mylist2[5])
    seconds_long = float(mylist2[6])
    dir_lat = str(mylist2[3])
    dir_long = str(mylist2[7])

    if dir_lat == "N":
        direction_lat = 1
    elif dir_lat == "S":
        direction_lat = -1
    else:
        direction_lat = 1

    if dir_long == "E":
        direction_long = 1
    elif dir_long == "W":
        direction_long = -1
    else:
        direction_long = 1
    
    dd_lat = direction_lat * (degrees_lat + (minutes_lat / 60) + (seconds_lat / 3600))
    dd_long = direction_long * (degrees_long + (minutes_long / 60) + (seconds_long / 3600))

    return dd_lat, dd_long
