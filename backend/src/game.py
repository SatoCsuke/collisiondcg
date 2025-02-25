from dataclasses import dataclass

# まだテストとかを書いてないので消しておく
#@dataclass
#class Field:
#  hand: list
#  battlefield: list
#  mana: list
#
#class Player:
#  def __init__(self, deck):
#    self.library = deck.mainboard
#    self.field = Field()
#
#class Creature:
#  def __init__(self, name, parameters, abilities):
#    self.name = name
#    self.parameter = parameter
#    self.abilities = abilities

@dataclass
class CreatureParameter:
  cost: int
  power: int
  toughness: int
  speed: int
