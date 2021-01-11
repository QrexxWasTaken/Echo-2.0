import time
import sys
import random
from colorama import Fore, Style, Back

#puberty related variables
puberty = False;
pubertyAge = random.randint(10,14);

#DEATH related variables
deathAge = random.randint(1,10);
finalDays = deathAge - random.randint(1,10);
deathCause = random.randint(1,5);

#----------------------------------------------#

if deathCause == 1:
	deathMessage = "Neo died of old age";
elif deathCause == 2:
	deathMessage = "Neo shot themself";
elif deathCause == 3:
	deathMessage = "Neo was murdered";
elif deathCause == 4:
	deathMessage = "Neo was killed in a car crash";
elif deathCause == 5:
	deathMessage = "Neo died of alcohol";

#----------------------------------------------#

#Marrige related variables
marriageAge = random.randint(16,40);
hasSpouse = False;
sexuality = random.randint(1,8)

#Socioeconomic related variables
wealth = random.randint(1,5);

#----------------------------------------------#

if wealth == 1:
	wealth = Fore.GREEN+"loaded"+Style.RESET_ALL;
elif wealth == 2:
	wealth = Fore.GREEN+"wealthy"+Style.RESET_ALL;
elif wealth == 3:
	wealth = Fore.YELLOW+"average"+Style.RESET_ALL;
elif wealth == 4:
	wealth = Fore.RED+"poor"+Style.RESET_ALL;
elif wealth == 5:
	wealth = Fore.RED+"homeless"+Style.RESET_ALL;

#----------------------------------------------#

print("Echo 2.0 v0.9.1a - Neo")

#----------------------------------------------#

for i in range(100):
	age = i;
	print("Neo is "+str(age)+" years old")
	time.sleep(1)
	if age == 0:
		print("Neo was born into a "+wealth+" family");
	if age == deathAge:
		print(".------------.")
		print("|   R.I.P.   |")
		print("|    Neo     |")
		print("|     "+str(age)+"      |")
		print("|____________|")
		print(deathMessage)
		sys.exit(Style.RESET_ALL+"Neo died "+wealth)
	age = age + 1;

