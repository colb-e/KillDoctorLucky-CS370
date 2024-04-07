import pygame

class States():
    def __init__(self, currentState):
        self.currentState = currentState
        self.stateStack = []
        self.previousState = None
        
    def getState(self):
        return self.currentState
    
    def enterState(self, state):
        if len(self.stateStack) > 1:
            self.previousState = self.stateStack[-1]
        self.currentState = state
        self.stateStack.append(state)
        
    def exitState(self):
        self.stateStack.pop()