
#!/usr/bin/env python3
with open ("dracula.txt", "r") as drac:
    count = 0
    for line in drac:
        if "vampire"  in line.lower():
            count += 1
            print(line)
        
            
