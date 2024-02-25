'''
Title: Room class file

Description: The purpose of this file is to create a class that will allow for an instance of each room withs its appropriate information to be stored
in an array to be easily accessed. The room x and y values should NEVER be updated. Players have been designed to update their location
within a room they enter it if there is a player already in the room, the given locations have been chosen to properly place four players
into a room at the same time.
'''
import pygame

class Rooms:
    # This will store the location of the stated room and the amount of people in the room
    # The room x and y will be the location of the player in the top left of the player group square 
    def __init__(self, roomX, roomY, room_count):
        self.roomX = roomX
        self.roomY = roomY
        self.room_count = room_count
        
    
roomsList = []
        
roomsList.append(Rooms(2, 1.8, 0)) # room 1
roomsList.append(Rooms(1.5, 1.7, 0)) # room 2
roomsList.append(Rooms(1.56, 2.7, 0)) # room 3
roomsList.append(Rooms(1.8, 2.75, 0)) # room 4
roomsList.append(Rooms(4.65, 3.5, 0)) # room 5
roomsList.append(Rooms(3.7, 1.6, 0)) # room 6
roomsList.append(Rooms(3.1, 1.07, 0)) # room 7
roomsList.append(Rooms(35, 1.2, 0)) # room 8
roomsList.append(Rooms(35, 1.4, 0)) # room 9
roomsList.append(Rooms(60, 1.9, 0)) # room 10
roomsList.append(Rooms(13, 4.8, 0)) # room 11
roomsList.append(Rooms(50, 15, 0)) # room 12
roomsList.append(Rooms(3.75, 8, 0)) # room 13
roomsList.append(Rooms(2.45, 25, 0)) # room 14
roomsList.append(Rooms(2.41, 8, 0)) # room 15
roomsList.append(Rooms(1.5, 25, 0)) # room 16
roomsList.append(Rooms(1.2, 25, 0)) # room 17
roomsList.append(Rooms(1.2, 4.5, 0)) # room 18
roomsList.append(Rooms(1.2, 1.9, 0)) # room 19
roomsList.append(Rooms(1.2, 1.35, 0)) # room 20
roomsList.append(Rooms(1.27, 1.2, 0)) # room 21
roomsList.append(Rooms(1.56, 1.1, 0)) # room 22
roomsList.append(Rooms(2.4, 1.1, 0)) # room 23
roomsList.append(Rooms(2, 1.55, 0)) # room 24