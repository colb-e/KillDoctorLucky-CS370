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
    def __init__(self, roomX1, roomY1, roomX2, roomY2, roomX3, roomY3, roomX4, roomY4, room_count):
        self.roomX1 = roomX1
        self.roomY1 = roomY1
        self.roomX2 = roomX2
        self.roomY2 = roomY2
        self.roomX3 = roomX3
        self.roomY3 = roomY3
        self.roomX4 = roomX4
        self.roomY4 = roomY4
        self.room_count = room_count
        
# This will store 4 setss of cords for each postion in the room for up to 4 players and also 
# store the amount of people in each room
roomsList = []
        
roomsList.append(Rooms(2.75, 1.9, 2.75, 1.7, 1.85, 1.93, 1.85, 1.7, 0)) # room 1
roomsList.append(Rooms(1.5, 1.93, 1.77, 1.93, 1.77, 1.52, 1.5, 1.52, 0)) # room 2
roomsList.append(Rooms(1.43, 3.4, 1.41, 2.5, 1.73, 2.5, 1.74, 3.3, 0)) # room 3
roomsList.append(Rooms(2.6, 3.4, 1.9, 3.6, 2, 2.4, 2.5, 2.3, 0)) # room 4
roomsList.append(Rooms(5, 3.5, 3, 3.2, 4.8, 2.6, 3.1, 2.5, 0)) # room 5
roomsList.append(Rooms(3.1, 1.52, 3.05, 1.9, 4.3, 1.9, 4.3, 1.54, 0)) # room 6
roomsList.append(Rooms(3.1, 1.07, 3.3, 1.4, 4.1, 1.35, 4.2, 1.08, 0)) # room 7
roomsList.append(Rooms(35, 1.2, 5, 1.15, 5.5, 1.05, 30, 1.07, 0)) # room 8
roomsList.append(Rooms(35, 1.4, 30, 1.27, 6.4, 1.28, 6.9, 1.4, 0)) # room 9
roomsList.append(Rooms(60, 1.9, 40, 1.6, 9, 1.55, 7, 1.7, 0)) # room 10
roomsList.append(Rooms(13, 4.8, 15, 2.7, 7, 2.6, 8, 4.4, 0)) # room 11
roomsList.append(Rooms(50, 15, 6.5, 13, 7.2, 7, 30, 6.5, 0)) # room 12
roomsList.append(Rooms(4.2, 8, 3.2, 6, 3.4, 25, 4, 25, 0)) # room 13
roomsList.append(Rooms(2.7, 25, 2.6, 12, 1.9, 23, 1.95, 12.2, 0)) # room 14
roomsList.append(Rooms(2.65, 7.85, 2.4, 4.9, 2.07, 5.2, 1.9, 7.3, 0)) # room 15
roomsList.append(Rooms(1.5, 25, 1.65, 25, 1.55, 6.5, 1.75, 7, 0)) # room 16
roomsList.append(Rooms(1.15, 25, 1.33, 14, 1.3, 7, 1.18, 6, 0)) # room 17
roomsList.append(Rooms(1.2, 4.5, 1.35, 3.6, 1.31, 2.5, 1.22, 2.7, 0)) # room 18
roomsList.append(Rooms(1.15, 1.9, 1.17, 1.55, 1.34, 1.8, 1.32, 1.6, 0)) # room 19
roomsList.append(Rooms(1.2, 1.41, 1.15, 1.41, 1.33, 1.275, 1.25, 1.275, 0)) # room 20
roomsList.append(Rooms(1.27, 1.21, 1.162, 1.125, 1.43, 1.15, 1.43, 1.06, 0)) # room 21
roomsList.append(Rooms(1.56, 1.1, 1.7, 1.05, 1.65, 1.4, 1.55, 1.35, 0)) # room 22
roomsList.append(Rooms(2.4, 1.1, 2.7, 1.2, 2.1, 1.27, 1.9, 1.15, 0)) # room 23
roomsList.append(Rooms(2, 1.59, 2, 1.5, 2.5, 1.5, 2.5, 1.59, 0)) # room 24


# Each list will represent a room and store the each room index that is adjacent to it 
adjacentRooms1 = [1, 3, 5, 23]
adjacentRooms2 = [0, 2, 3, 17, 18, 20, 21]
adjacentRooms3 = [1, 3, 15, 16, 17, 18, 20]
adjacentRooms4 = [0, 1, 2, 4, 5, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20]
adjacentRooms5 = [3, 10, 11, 12, 5, 7, 9]
adjacentRooms6 = [0, 6, 3, 4, 7, 9, 10, 11]
adjacentRooms7 = [7, 5, 21, 22, 23,]
adjacentRooms8 = [6, 8, 3, 4, 5, 9, 10, 11]
adjacentRooms9 = [7, 9]
adjacentRooms10 = [8, 3, 4, 5, 7, 10, 11]
adjacentRooms11 = [3, 4, 5, 7, 9, 11, 12]
adjacentRooms12 = [10, 12, 3, 4, 5, 7, 9]
adjacentRooms13 = [3, 4, 10, 11, 13, 14]
adjacentRooms14 = [12, 14, 15]
adjacentRooms15 = [12, 13, 15, 3]
adjacentRooms16 = [13, 14, 2, 3, 16, 17]
adjacentRooms17 = [2, 3, 15, 17, 1, 18, 20]
adjacentRooms18 = [2, 3, 15, 16, 1, 18, 20]
adjacentRooms19 = [19, 1, 2, 3, 17, 20]
adjacentRooms20 = [18, 20]
adjacentRooms21 = [21, 19, 1, 2, 3, 17, 18, 20]
adjacentRooms22 = [1, 20, 6, 22, 23]
adjacentRooms23 = [6, 21, 23]
adjacentRooms24 = [0, 6, 21, 22]



allAdjacentRooms = [adjacentRooms1, adjacentRooms2, adjacentRooms3, adjacentRooms4, adjacentRooms5, adjacentRooms6, adjacentRooms7, adjacentRooms8, adjacentRooms9, adjacentRooms10, adjacentRooms11, adjacentRooms12,
                    adjacentRooms13, adjacentRooms14, adjacentRooms15, adjacentRooms16, adjacentRooms17, adjacentRooms18, adjacentRooms19, adjacentRooms20, adjacentRooms21, adjacentRooms22, adjacentRooms23, adjacentRooms24]

