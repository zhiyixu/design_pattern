from abc import ABC, abstractmethod


class Player(object):

    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body 
        self.arm  = arm 
        self.leg = leg 

    def __repr__(self):
        return f"<Player(face={self.face}, body={self.body}, arm={self.arm}, leg={self.leg})>"
    

class PlayerBuilder(ABC):

    @abstractmethod
    def build_face(self): ...

    @abstractmethod
    def build_body(self): ...

    @abstractmethod
    def build_arm(self): ...

    @abstractmethod
    def build_leg(self): ...


class FemaleBuilder(PlayerBuilder):

    def __init__(self):
        self.player = Player() 

    def build_face(self):
        self.player.face = "Female face"

    def build_body(self):
        self.player.body = "Female body"

    def build_arm(self):
        self.player.arm = "Female arm"

    def build_leg(self):
        self.player.leg = "Female leg"


class MaleBuilder(PlayerBuilder):

    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "Male face."

    def build_body(self):
        self.player.body = "Male body"

    def build_arm(self):
        self.player.arm = "Male arm"

    def build_leg(self):
        self.player.leg = "Male leg"


class PlayerDirector(object):

    """
    control the squence of builder
    """
    def build_player(self, builder: PlayerBuilder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player

# --- # 

builder = MaleBuilder()
director = PlayerDirector()
p = director.build_player(builder)
print(p)