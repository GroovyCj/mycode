#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  print(rooms[currentRoom]['desc'])
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key',
                  'desc'  : 'A long corridor filled with gothic paintings, you see an image of a pale orphan, her eyes seem to follow you.  To the South lies a Kitchen and the East a Dining Room.'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                  'desc'  : 'There are numerous pots filled with a strange viscous fluid, a rancid odor fills the room. Back North leads to the Hall.'
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
                  'desc' : 'A painting of a family sits above the dining table, the father\'s gaze pieces through you. To the West is the Hall, South leads to a Garden, and North is a Pantry.'
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'south' : 'Shed',
                  'desc'  : 'A winding maze filled with poisonous plants, the bushes shutter and groan as you pass. Back North leads to the Dining Room. looking South you see a crumbling Shed'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'Severed Eye',
                  'desc' : 'You see odd looking items, nothing looks edible.  Back south leads to the Dining Room.'
            },

            'Shed' : {
                
                'desc'  : 'You enter a dilapidated shed, the door slams behind you, you are locked in.. the light flickers around you.',
                'item'  : 'ceremonial knife'
                

            }


         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break

  elif 'ceremonial knife' in inventory:
    print('The knife shakes violently, and impales you in the chest... an ominious figure appears as your vision fades... Game Over..')
    break
