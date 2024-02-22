import pygame

class Rooms:
    # This will store the location of the stated room and the amount 
    # of people in the room
    def __init__(self, roomX, roomY, room_count):
        self.roomX = roomX
        self.roomY = roomY
        self.room_count = room_count
        
    
roomsList = []
        
roomsList.append(Rooms(2, 1.8, 0)) # room 1
roomsList.append(Rooms(1.5, 1.7, 0)) # room 2
        
   