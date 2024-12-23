import csv

toanalyze = []
driverkey = {}
key = '\n Max Verstappen = VER \n Lewis Hamilton = HAM \n George Russell = RUS \n Charles Leclerc = LEC \n Carlos Sainz = SAI \n Valtteri Bottas = BOT \n Zhou Guanyu = ZHO \n Fernando Alonso = ALO \n Lance Stroll = STR \n Sergio \'Checo\' Perez = PER \n Oscar Piastri = PIA \n Lando Norris = NOR \n Sebastian Vettel = VET \n Daniel Riccardo = RIC \n Yuki Tsunoda = TSU \n Liam Lawson = LAW \n Esteban Ocon = OCO \n Oliver Bearman = BEA \n Pierre Gasly = GAS \n Nico Hulkenberg = HUL \n Kevin Magnussen = MAG \n Alexander Albon = ALB \n Logan Sargeant = SAR \n Franco Colapinto = COL \n Daniil Kyvat = KYV \n Romain Grosjean = GRO\n Jack Aitken = AIT \n Nyck De Vries = DEV \n Marcus Erricson = ERI \n Pietro Fittipaldi = FIT \n Antonio Giovinazzi = GIO \n Brendon Hartley = HAR \n Robert Kubica = KUB \n Nicholas Latifi = LAT \n Nikita Mazepin = MAZ \n Mick Schumacher = MSC \n Kimi Raikonen = RAI \n Sergey Sirotkin = SIR \n Jack Doohan = DOO \n Andrea Kimi Antonelli = ANT \n Isack Hadjar = HAD \n Gabriel Bortoleto = BOR \n'

pts = [25,18,15,12,10,8,6,4,2,1]

def csvthing():
    file=open("f1.CSV", "r")
    reader = csv.reader(file)
    for line in reader:
        temp = [line[3], line[4], line[5], line[6], line[7],line[8], line[9], line[10], line[11], line[12]]

        temp2 = []

        for i in range(len(temp)):
            x = float(temp[i])
            temp2.append(x)

        driverkey[line[0]] = temp2
    
    #print(driverkey)


def choosedriver():
    x = input("welcome. first, type Y if you would like the list of drivers and their key, or anything else if you already know their 3 letter key: ")

    if (x == "Y" or x == "y"):
        print(key)
    
    return input("please enter the three letter key for the driver: ").upper()

def printavgall(d):
    x = 0.0
    for i in range(len(driverkey[d])):
        x = x + (driverkey[d][i] * pts[i])
    
    
    print("\n"+d + "'s average point score across every active season since 2018 is: "+ str(x) + " points")

def printavgplaces(d):
    print("roughly, the average times (percentage) that "+d+" has placed in the top 10 in every active season since 2018 is as follows:\n")

    x = 0

    for i in range(len(driverkey[d])):
        print(str(i+1) +": "+ str(driverkey[d][i] * 100)+"%")

        x = x + driverkey[d][i]
        
    print("\nthe percentage chance of this driver landing within the points (top 10) is: "+str(x) + "%")


def main():
    run = True

    while(run): 
        csvthing()
        driver = choosedriver()
        printavgall(driver)
        printavgplaces(driver)

        x = input("\nwould you like to search for another driver? Type 'N' if no, type anything else to continue: ")

        if (x.upper() == 'N'):
            run = False

main()
