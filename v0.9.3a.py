import time
import sys
import random
from colorama import Fore, Style, Back

wealth = random.randint(1, 5)

#everyday life related variables
driveTest = random.randint(1, 10)
canDrive = False
canAfford = True;

#----------------------------------------------#

if driveTest >= 8:
    driveTestPass = "passed " + Fore.GREEN + "with flying colors" + Style.RESET_ALL
    canDrive = True
	
elif driveTest <= 7:
    if driveTest >= 5:
        driveTestPass = Fore.YELLOW + "barely " + Style.RESET_ALL + "passed"
        canDrive = True
    else:
        pass
else:
    driveTestPass = Fore.RED + "didn't pass" + Style.RESET_ALL

if wealth >= 3:
		canAfford = False;
		if canDrive == True:
			canDrive = False;
		affordMessage = "But Neo is too poor and "+Fore.RED+"cannot afford a car"+Style.RESET_ALL;
else:
		canAfford = True;
		affordMessage = "Neo now "+Fore.GREEN+"has a car"+Style.RESET_ALL;

#----------------------------------------------#

#addiction related variables
alcoholTry = random.randint(1, 5)
aAddictionProbability = random.randint(1, 5)

#----------------------------------------------#

if alcoholTry == 1:
    alcoholTry = Fore.GREEN + "great" + Style.RESET_ALL
    aAddictionProbability += 2
elif alcoholTry == 2:
    alcoholTry = Fore.GREEN + "good" + Style.RESET_ALL
    aAddictionProbability += 1
elif alcoholTry == 3:
    alcoholTry = Fore.YELLOW + "ok" + Style.RESET_ALL
    aAddictionProbability += 0
elif alcoholTry == 4:
    alcoholTry = Fore.RED + "bad" + Style.RESET_ALL
    aAddictionProbability -= 1
elif alcoholTry == 5:
    alcoholTry = Fore.RED + "terrible" + Style.RESET_ALL
    aAddictionProbability -= 2

#----------------------------------------------#

if aAddictionProbability >= 4:
    aAddictionProb = Fore.RED + "is likely" + Style.RESET_ALL
elif aAddictionProbability <= 3:
    if aAddictionProbability > 0:
        aAddictionProb = Fore.YELLOW + "is not likely" + Style.RESET_ALL
    else:
        pass
elif aAddictionProbability <= 0:
    aAddictionProb = Fore.GREEN + "will never" + Style.RESET_ALL

#----------------------------------------------#

#puberty related variables
puberty = False
pubertyAge = random.randint(10, 14)
pubertyEndAge = random.randint(pubertyAge + 1, 20)
attractiveness = random.randint(1, 5)

#----------------------------------------------#

if attractiveness == 1:
    attractiveness = Fore.GREEN + "beautiful" + Style.RESET_ALL
elif attractiveness == 2:
    attractiveness = Fore.GREEN + "attractive" + Style.RESET_ALL
elif attractiveness == 3:
    attractiveness = Fore.YELLOW + "average" + Style.RESET_ALL
elif attractiveness == 4:
    attractiveness = Fore.RED + "revolting" + Style.RESET_ALL
elif attractiveness == 5:
    attractiveness = Fore.RED + "revolting" + Style.RESET_ALL

#----------------------------------------------#

#DEATH related variables
deathAge = random.randint(1, 25)
finalDays = deathAge - random.randint(1, 10)
deathCause = random.randint(1, 5)

#----------------------------------------------#

if deathCause == 1:
    deathMessage = "Neo died of natural causes"
elif deathCause == 2:
    deathMessage = "Neo shot themself"
elif deathCause == 3:
    deathMessage = "Neo was murdered"
elif deathCause == 4:
    deathMessage = "Neo was killed in a car crash"
elif deathCause == 5:
    deathMessage = "Neo died of alcohol poisoning"

#----------------------------------------------#

#Marrige related variables
marriageAge = random.randint(16, 40)
hasSpouse = False
sexuality = random.randint(1, 8)

#----------------------------------------------#

if sexuality == 1:
    sexuality = Fore.YELLOW + "homosexual" + Style.RESET_ALL
else:
    sexuality = Fore.YELLOW + "heterosexual" + Style.RESET_ALL

#----------------------------------------------#

#Socioeconomic related variables

#----------------------------------------------#

if wealth == 1:
    wealth = Fore.GREEN + "loaded" + Style.RESET_ALL
elif wealth == 2:
    wealth = Fore.GREEN + "wealthy" + Style.RESET_ALL
elif wealth == 3:
    wealth = Fore.YELLOW + "average" + Style.RESET_ALL
elif wealth == 4:
    wealth = Fore.RED + "poor" + Style.RESET_ALL
elif wealth == 5:
    wealth = Fore.RED + "homeless" + Style.RESET_ALL

#----------------------------------------------#

print("Echo 2.0 v0.9.1a - Neo")

#----------------------------------------------#

for i in range(100):
    age = i
    print("Neo is " + str(age) + " years old")
    time.sleep(1)
    if age == 0:
        print("Neo was born into a " + wealth + " family")
    if age == deathAge:
        print(".------------.")
        print("|   R.I.P.   |")
        print("|    Neo     |")
        print("|     " + str(age) + "     |")
        print("|____________|")
        print(deathMessage)
        sys.exit(Style.RESET_ALL + "Neo died " + wealth)
    if age == pubertyAge:
        print("Neo is " + str(age) + " and is going into " + Fore.YELLOW +
              Back.WHITE + "puberty" + Style.RESET_ALL)
        puberty = True
        time.sleep(1)
    if age == pubertyEndAge and puberty == True:
        print("Neo is now " + str(age) + " and is finished with " +
              Fore.YELLOW + Back.WHITE + "puberty" + Style.RESET_ALL)
        time.sleep(1)
        print("Neo is " + sexuality);
        time.sleep(1);
        print("Neo looks " + attractiveness);
    if age == 16:
        print("Neo tested for a drivers' license");
        time.sleep(1);
        print("Neo " + driveTestPass);
        print(affordMessage)
    if age == 21:
        print("Neo tried alcohol for the first time\nIt went " + alcoholTry)
        time.sleep(.75)
        print("Neo "+aAddictionProb+" to get addicted to alcoholic beverages")
    age = age + 1
