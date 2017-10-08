'''
Created on Oct 5, 2017

@author: Jason
'''

import os

class Player:
    def __init__(self, name):
        """
        Builds the player object with name and sets the bank from file
        Args:
            None
        Returns:
            None
        """
        self.name = name
        self.bank = 0
        self.setBank()
        
    def setBank(self):
        """
        Retrieves bank amount from file
        Args:
            None
        Returns:
            None
        """
        bankFile = open("BankFile.txt", "r")
        for line in bankFile:
            pieces = line.split()
            if pieces[0] == self.name:
                self.bank = float(pieces[1])
                break
        bankFile.close()
        
        if self.bank == 0:
            bankFile = open("BankFile.txt", "a")
            bankFile.write("\n" + self.name + " " + str(50))
            self.bank = float(50)
            bankFile.close()
    
    def saveBank(self):
        """
        Saves the bank amount back to the file
        Args:
            None
        Returns:
            None
        """
        bankFile = open("BankFile.txt", "r")
        tempFile = open("BankFile.tmp", "w")
        for line in bankFile:
            pieces = line.split()
            if pieces[0] == self.name:
                tempFile.write(self.name + " " + str(self.bank) + "\n")
            else:
                tempFile.write(line)
        tempFile.close()
        bankFile.close()
        
        os.remove("BankFile.txt")
        os.rename("BankFile.tmp", "BankFile.txt")
        
