#!/usr/bin/env python3
import shutil
import os
def main():
    # forces python to start program in home user directory 
    os.chdir("/home/student/mycode/")
    # copies data from fileA to FileB source to destination
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    #copies folders and files from source to destination
    shutil.copytree("5g_research/", "5g_research_backup/")
main()
