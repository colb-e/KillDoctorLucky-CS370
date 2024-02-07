import pygame

class Rooms:
    
    #later we should add dedicated cords for dr lucky to have in each room
    #Later when we have to implement multiplayer we should subtract or add to the given values if a player enters a room with more than one player
    def __init__(self, room_num, room_x, room_y):
        self.room_num = room_num
        self.room_x = room_x
        self.room_y = room_y


    def setRooms():
        room5 = Rooms(5, 4.75, 4)