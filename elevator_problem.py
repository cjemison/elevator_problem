__author__ = 'Cornelius Jemison <cornelius.jemison@gmail.com>'

import sys
from lib.building import Building
from lib.instruction import InstructionSet


def main(filename):
    """This elevator problem uses the factory and strategy pattern to traverse floors.
    """
    if filename:
        l = list()
        with open(filename, 'rb') as file:
            for line in file.readlines():
                l.append(InstructionSet(line.rstrip("\n")))

        # validate instructions.
        building = Building()
        for item in l:
            for call in item.calls:
                call.validate_instruction(building.number_of_floors)

        # run model a
        for item in l:
            building.elevator.set_current_floor_number(item.current_floor)
            building.elevator.process_instructions(item.calls)
            print building.elevator.output()

        print ''

        # run model b
        building.set_elevator_factory("MODEL_B")
        for item in l:
            building.elevator.set_current_floor_number(item.current_floor)
            building.elevator.process_instructions(item.calls)
            print building.elevator.output()

if __name__ == "__main__":
    main(sys.argv[1])
