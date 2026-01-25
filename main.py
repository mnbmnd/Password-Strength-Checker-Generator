########################################################
# Author: Muneeb Mennad                                #
# Project Name: Password Strength Checker              #
# File Name: main.py                                   #
# Date: 2026-01-24                                     #
# Github Username: pchstpch                            #
########################################################


# import math
# import string
import entropy
# import password_generator

if __name__ == "__main__":
    print("PASSWORD STRENGTH CHECKER")
    userPassword = input("Please enter your password: ")
    print("Password length: " + str(entropy.getSize(userPassword)))
    print("Upper count: " + str(entropy.getUppercaseCount(userPassword)))
    print("Lower count: " + str(entropy.getLowercaseCount(userPassword)))
    print("Numeric count: " + str(entropy.getNumericCount(userPassword)))
    print("Symbols count: " + str(entropy.getSymbolsCount(userPassword)))
    print("Space count: " + str(entropy.getSpaceCount(userPassword)))
    
    print("Entropy: {:.1f}".format(entropy.getEntropy(userPassword)))
    print("Time to crack (in years): {:.1f}".format(entropy.getTimeToCrack(userPassword)))
    
    
    
# end main
# WIP