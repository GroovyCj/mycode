#!/usr/bin/env python3


def main():


    Geralt={'Homeland':'Rivia','School':'Wolf','Armor':'Bear','Wife':'Yennefer','Age':104,'Spells':['Aard','Yrden','Igni','Quen','Axii']}


    Geralt["Daughter"] = "Ciri";

    print(Geralt.keys())
    choice =  input("Please select a key from above NOTE: it is case sensitive\n")

    print(f"Geralts {choice} is: {Geralt[choice]} " )









main();    



