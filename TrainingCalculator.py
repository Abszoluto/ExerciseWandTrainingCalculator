"""
    * Version 1.1 - Added the percentage of current magic level to the count of wands
    * Version 2.0 - Added compatibility for loyalty points
    * Version 2.2 - Personal dummy now avaliable for the calculus
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

def verifyLoyalty(loyaltyPoints):
    if loyaltyPoints < 0 or loyaltyPoints > 3600:
        return 0
    else:
        return float(((loyaltyPoints/360) * 5)/100)

manaPerWand = 302000 # Ammount of mana that you "will spend" using one wand
baseManaMl = 1600 # This is the base mana ammount to get to ml 2
manaNeeded = 0 # This will be the ammount of mana needed for the target magic level
manaAlreadySpent = 0 # This will be the already spent mana in your current magic level
try:
    atualMl = input("What is your magic level now ? ")
    atualPercentage = input("What is the percentage progress in your current magic level ? ")
    desiredMl =  input("What is the desired magic level? ")
    doubleExpStatus = verifyStatus(input("Is it double exp ? "))
    loyaltyPointsAmmount = int(input("What is the ammount of loyalty points (0 if none)? "))
    personalDummy = verifyStatus(input("Do you have a personal dummy ? "))
    counterManaAtualMl = int(atualMl) - 1

    #   This while calculates the ammount of mana you've already spent in your magic Level
    while counterManaAtualMl:
        manaAlreadySpent = manaAlreadySpent + baseManaMl
        baseManaMl = ((baseManaMl/100) * 10) + baseManaMl
        counterManaAtualMl = counterManaAtualMl -1
    counterManaTargetMl = int(desiredMl) - 1

    #   Magic level current percentage added to manaAlreadySpent
    manaAlreadySpent = manaAlreadySpent + (baseManaMl*(float(atualPercentage)/100))

    #   Loyalty points calculator based on the ammount of mana already spent
    manaAlreadySpent = manaAlreadySpent +(manaAlreadySpent*verifyLoyalty(loyaltyPointsAmmount))
    baseManaMl = 1600

    #   This while calculates the ammount of mana needed for the target magic level
    while counterManaTargetMl:
        manaNeeded = manaNeeded + baseManaMl
        tmp = (baseManaMl/100) * 10
        baseManaMl = baseManaMl + tmp
        counterManaTargetMl = counterManaTargetMl - 1

    #   This calculates the whole mana needed to target magic level and it will be rounded to make things easier to read
    manaNeeded = round(manaNeeded - manaAlreadySpent)

    # If doubleExp is active, the ammount of mana needed for the next ML is divided by two
    if doubleExpStatus:
        manaNeeded = manaNeeded / 2
    wandsNeeded = manaNeeded/302000

    """
        * The condition below are related if the player has a personal dummy,
        if it has, and it is double exp: 20% improve on the training (0,2 * wandsNeeded)
        if it has, but the double exp its off: 10% improve on the training (0,1 * wandsNeeded)
        Since we need to know the number of wands that we need, our training will be more effective
        with less wands, so (wandsNeeded - (0,2 * wandsNeeded) or (0,1 * wandsNeeded))
    """
    if personalDummy:
        if doubleExpStatus:
            wandsNeeded = wandsNeeded - (wandsNeeded * 0.2)
        else:
            wandsNeeded = wandsNeeded - (wandsNeeded *0.1)
    print (f"Mana needed for the Magic Level {desiredMl}: {manaNeeded}")
    print(f"Wands needed for get the desired Magic Level: {wandsNeeded}")
except:
        print("Im sorry, an error has ocurred...")
