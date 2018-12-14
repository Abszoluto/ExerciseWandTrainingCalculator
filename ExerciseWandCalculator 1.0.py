"""
    * This program was made to calculate how many training Wands and Rods you need to acquire the desired Magic Level
    * Made in Python 3.7.0
    * Author: Abszoluto
"""
def verifyStatus (status):
    """
        This method is responsable for validating the user answer depending on the main language
    """
    if (status.lower() == "yes") or (status.lower() == "sim") or (status == "1"):
        return True
    else:
        return False


manaPerWand = 302000 # Ammount of mana that you "will spend" using one wand
baseManaMl = 1600 # This is the base mana ammount to get to ml 2
manaNeeded = 0 # This will be the ammount of mana needed for the target magic level
manaAlreadySpent = 0 # This will be the already spent mana in your current magic level

try:
    atualMl = input("What is your magic level now ? ")
    desiredMl =  input("What is the desired magic level? ")
    doubleExpStatus = verifyStatus(input("Is it double exp ? "))
    counterManaAtualMl = int(atualMl) - 1

    # This while calculates the ammount of mana you've already spent in your magic Level
    while counterManaAtualMl:
        manaAlreadySpent = manaAlreadySpent + baseManaMl
        baseManaMl = ((baseManaMl/100) * 10) + baseManaMl
        counterManaAtualMl = counterManaAtualMl -1

    counterManaTargetMl = int(desiredMl) - 1
    baseManaMl = 1600

    #This while calculates the ammount of mana needed for the target magic level
    while counterManaTargetMl:
        manaNeeded = manaNeeded + baseManaMl
        tmp = (baseManaMl/100) * 10
        baseManaMl = baseManaMl + tmp
        counterManaTargetMl = counterManaTargetMl - 1

    #This calculates the whole mana needed to target magic level and it will be rounded to make things easier to read
    manaNeeded = round(manaNeeded - manaAlreadySpent)

    # If doubleExp is active, the ammount of mana needed for the next ML is divided by two
    if doubleExpStatus:
        manaNeeded = manaNeeded / 2
    print (f"Mana needed for the Magic Level {desiredMl}: {manaNeeded}")
    wandsNeeded = manaNeeded/302000
    print(f"Wands needed for get the desired Magic Level: {wandsNeeded}")
except:
    print("Im sorry, an error has ocurred...")
