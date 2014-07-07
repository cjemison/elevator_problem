__author__ = 'Cornelius Jemison <cornelius.jemison[@]gmail.com>'


import sys
sys.path.append("../")
import unittest
from lib.building import Building
from lib.instruction import InstructionSet
from lib.instruction import Instruction


class TestUM(unittest.TestCase):

    def setUp(self):
        self.building = Building()
        self.data = """10:8-1|9:1-5,1-6,1-5|2:4-1,4-2,6-8|3:7-9,3-7,5-8,7-11,11-1|7:11-6,10-5,6-8,7-4,12-7,8-9|6:1-8,6-8"""

    def test_model_a(self):
        self.building.set_elevator_factory("MODEL_A")
        model_a_expected_result = [9, 30, 16, 36, 40, 16]
        for idx, item in enumerate(self.data.split("|")):
            i = InstructionSet(item)
            self.building.elevator.set_current_floor_number(i.current_floor)
            self.building.elevator.process_instructions(i.calls)
            self.assertEqual(model_a_expected_result[idx], self.building.elevator.floors_traveled)

    def test_model_b(self):
        self.building.set_elevator_factory("MODEL_B")
        model_b_expected_result = [9, 13, 12, 18, 30, 12]
        for idx, item in enumerate(self.data.split("|")):
            i = InstructionSet(item)
            self.building.elevator.set_current_floor_number(i.current_floor)
            self.building.elevator.process_instructions(i.calls)
            self.assertEqual(model_b_expected_result[idx], self.building.elevator.floors_traveled)

    def test_instructions_for_letters(self):
        flag = False
        try:
            i = Instruction("a", "b")
            i.validate_instruction(12)
        except Exception:
            flag = True
        self.assertEqual(flag, True)

    def test_instructions_for_zeros(self):
        flag = False
        try:
            i = Instruction(0, 0)
            i.validate_instruction(12)
        except Exception:
            flag = True
        self.assertEqual(flag, True)

if __name__ == '__main__':
    unittest.main()
