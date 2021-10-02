class Player:
    def __init__(self):
        self.character = -1
        self.background = -1
        pass


    def pickCharacter(self, selection):
        self.character = selection
        pass
        


    def pickBackground(self, selection):
        self.background = selection
        pass

class Level:
    def __init__(self, cSelectionScreen, bSelectionScreen):
        self.cSelectionScreen = 0 
        self.bSelectionScreen = 0
    def showCScreen():
        pass
    def showBScreen(next):
        pass

class Buttons:
    def __init__(self, label, width, height, x, y):
        self.label = label
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw():
        pass

    def click():
        pass

class Fighter:
    def __init__(self, x, y, costumeList, soundList):
        self.x=x
        self.y=y
        self.costumeList = costumeList
        self.soundList = soundList

    def draw(self):
        pass



class Eren(Fighter):
    def __init__(self):
        pass

    
    
