import pygame

class Rooms:
    
    #later we should add dedicated cords for dr lucky to have in each room
    #Later when we have to implement multiplayer we should subtract or add to the given values if a player enters a room with more than one player
    def __init__(self, room_x, room_y):
        self.room_x = room_x
        self.room_y = room_y

    def createRooms():

        rooms = []

        # Room cords
        # order of rooms from 1-24
        rooms.append(Rooms(2, 2)) # room 1
        rooms.append(Rooms(1.35, 2)) # room 2
        rooms.append(Rooms(1.28, 2.75)) # room 3
        rooms.append(Rooms(1.7, 2.75)) # room 3
        rooms.append(Rooms(4.75, 4)) # room 5
        rooms.append(Rooms(2.8, 1.75)) # room 6
        rooms.append(Rooms(2.8, 1.5)) # room 7
        rooms.append(Rooms(4.5, 1.25)) # room 8
        rooms.append(Rooms(5.7, 1.5)) # room 9
        rooms.append(Rooms(5.9, 1.7)) # room 10
        rooms.append(Rooms(13, 5)) # room 11
        rooms.append(Rooms(5.85, 6.9)) # room 12
        rooms.append(Rooms(3.75, 7.1)) # room 13
        rooms.append(Rooms(2.45, 25)) # room 14
        rooms.append(Rooms(2.41, 8)) # room 15
        rooms.append(Rooms(1.58, 7)) # room 16
        rooms.append(Rooms(1.2, 25)) # room 17
        rooms.append(Rooms(1.2, 5)) # room 18
        rooms.append(Rooms(1.03, 2.1)) # room 19
        rooms.append(Rooms(1.2, 1.57)) # room 20
        rooms.append(Rooms(1.2, 1.34)) # room 21
        rooms.append(Rooms(1.35, 1.32)) # room 22
        rooms.append(Rooms(1.67, 1.32)) # room 23
        rooms.append(Rooms(2, 1.66)) # room 24
        return rooms