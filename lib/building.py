__author__ = 'Cornelius Jemison <cornelius.jemison[@]gmail.com>'

from elevators import ElevatorFactory


class Building(object):
    """This is class represents a building."""

    def __init__(self, number_of_floors=12, elevator_type="MODEL_A"):
        self._number_of_floors = number_of_floors
        self._elevator = ElevatorFactory.build_elevator(number_of_floors, elevator_type)

    @property
    def elevator(self):
        return self._elevator

    @property
    def number_of_floors(self):
        return self._number_of_floors

    def set_elevator_factory(self, elevator_type):
        self._elevator = ElevatorFactory.build_elevator(self._number_of_floors, elevator_type)
