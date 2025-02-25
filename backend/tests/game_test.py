import pytest
from src.game import CreatureParameter

def test_parameter():
  cost, power, toughness, speed = 1, 1, 1, 1
  p = CreatureParameter(cost, power, toughness, speed)

  assert cost == p.cost
  assert power == p.power
  assert toughness == p.toughness
  assert speed == p.speed