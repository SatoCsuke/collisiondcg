import pytest
from src.game import CreatureParameter, FieldCreature

mock_goblin_parameter = CreatureParameter(1, 1 ,1 ,1)
mock_field_goblin = FieldCreature(
  name="Goblin",
  parameter=mock_goblin_parameter,
  abilities=[]
)

def test_parameter():
  cost, power, toughness, speed = 1, 1, 1, 1
  p = CreatureParameter(cost, power, toughness, speed)

  assert cost == p.cost
  assert power == p.power
  assert toughness == p.toughness
  assert speed == p.speed

def test_field_creature():
  assert "Goblin" == mock_field_goblin.name
  assert 1 == mock_field_goblin.params.cost
  assert 1 == mock_field_goblin.params.power
  assert 1 == mock_field_goblin.params.toughness
  assert 1 == mock_field_goblin.params.speed
  assert True == mock_field_goblin.summonsick