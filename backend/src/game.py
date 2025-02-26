from dataclasses import dataclass
from abc import ABC, abstractmethod

# playerが全てを持っている感じにする？
# abilityはtargetに対して影響を与えるようにする
#@dataclass
#class Field:
#  hand: list
#  battlefield: list
#  manafield: list
#  library: list
#
#  @property
#  def mainboard(self):
#    return self.library.mainboard
#
#  @property
#  def sideboaerd(self):
#    return self.library.sideboard

class FieldObject(ABC):
  def __init__(self):
    pass

class FieldCreature(FieldObject):
  def __init__(self, name, parameter, abilities):
    self.name = name
    self.params = parameter
    self.abilities = abilities
    self.summonsick = True

# カードから先に定義すると訳わからなくなるのでフィールドオブジェクトから先に定義したほうが良さげ
#class Card(ABC):
#  def __init__(self, name, parameter, abilities):
#    self.name = name
#    self.parameter = parameter
#    self.abilities = abilities
#
#  @abstractmethod
#  def play(self):
#    pass

#class Player:
#  def __init__(self, life_point):
#    self.field = Field()
#    self.lp = life_point
#
#class CreatureCard(Card):
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

#class Ability(ABC):
#  @abstractmethod
#  def affect(self, target):
#    pass
#
#class Haste(ability):
#  def affect(self, field_creature):
#    field_creature.summonsick = false
#    return field_creature