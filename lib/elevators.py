__author__ = 'Cornelius Jemison <cornelius.jemison[@]gmail.com>'

from operator import attrgetter

class Elevator(object):
    """This class represent a elevator, which traverses building floors."""

    def __init__(self, number_of_floors):
        self._building_floors = number_of_floors
        self._floors_traveled = 0
        self._current_floor_number = 0
        self._final = list()

    @property
    def floors_traveled(self):
        return self._floors_traveled

    def set_current_floor_number(self, current_floor_number):
        self._current_floor_number = current_floor_number
        self._floors_traveled = 0
        self._final = list()

    def _go_up(self, stopping_point):
        while self._current_floor_number < stopping_point:
            self._floors_traveled += 1
            self._current_floor_number += 1

    def _go_down(self, stopping_point):
        while self._current_floor_number > stopping_point:
            self._floors_traveled += 1
            self._current_floor_number -= 1

    def _move_elevator(self, stoping_point):
        if self._current_floor_number < stoping_point:
            self._go_up(stoping_point)
        else:
            self._go_down(stoping_point)

    def process_instructions(self, instruction_list):
        raise NotImplemented("This method hasn't been implemented.")

    def output(self):
        return "%s (%d)" % (" ".join([ str(x) for x in self._final]), self._floors_traveled,)


class ModelAElevator(Elevator):
    """This is the model a elevator."""

    def __init__(self, number_floors):
        Elevator.__init__(self, number_floors)

    def process_instructions(self, instruction_list):
        if self._current_floor_number != instruction_list[0].start_position:
            self._final.append(self._current_floor_number)

        for item in instruction_list:
            self._move_elevator(item.start_position)
            self._move_elevator(item.end_position)
            self._final.append(item.start_position)
            self._final.append(item.end_position)
        self.output()


class ModelBElevator(Elevator):
    """This is the model b elevator."""

    def __init__(self, number_floors):
        Elevator.__init__(self, number_floors)

    def _get_unique_values(self, l, reverse=False):
        tmp_list = list()
        if l:
            for item in l:
                if item.start_position not in tmp_list:
                    tmp_list.append(item.start_position)
                if item.end_position not in tmp_list:
                    tmp_list.append(item.end_position)
            tmp_list = sorted(set(tmp_list), reverse=reverse)
        return tmp_list

    def _sort_instructions(self, l, reverse=False):
        tmp_list = list()
        if l:
            tmp_list = sorted(tmp_list, key=attrgetter("start_position", "end_position"), reverse=reverse)
        return tmp_list

    def _switch_directions(self, instruction):
        return instruction.start_position < instruction.end_position

    def process_instructions(self, instruction_list):
        if instruction_list:
            # remove duplicates and retain original order
            unique = list()
            [unique.append(item) for item in instruction_list if item not in unique]
            tmp_list = list()
            previous_item = None
            for item in unique:
                if not previous_item:
                    # the list is empty.
                    tmp_list.append(item)
                elif ((previous_item.start_position < previous_item.end_position
                       and item.start_position < item.end_position)
                       or (previous_item.start_position > previous_item.end_position
                       and item.start_position > item.end_position)):
                    # previous instruction was the same so add to list.
                    tmp_list.append(item)
                else:
                    # change directions
                    flag = self._switch_directions(tmp_list[0])
                    if flag:
                        tmp_list = sorted(tmp_list, key=attrgetter("start_position", "end_position"))
                        l1 = self._get_unique_values(tmp_list)
                        self._final.extend(l1)
                        tmp_list = list()
                        tmp_list.append(item)

                    else:
                        tmp_list = sorted(tmp_list, key=attrgetter("start_position", "end_position"), reverse=True)
                        l1 = self._get_unique_values(tmp_list, True)
                        self._final.extend(l1)
                        tmp_list = list()
                        tmp_list.append(item)
                previous_item = item

            # catch any remaining instructions not processed.
            if tmp_list:
                flag = self._switch_directions(tmp_list[0])
                if flag:
                    l1 = self._get_unique_values(tmp_list)
                    self._final.extend(l1)
                else:
                    l1 = self._get_unique_values(tmp_list, True)
                    self._final.extend(l1)

            # set the current floor if the current_floor
            if self._current_floor_number != self._final[0]:
                 self._final.insert(0, self._current_floor_number)

            # move elevator
            self._current_floor_number = self._final[0]
            for x in self._final[1:]:
                self._move_elevator(x)
            self.output()


class ElevatorFactory(object):
    """This class represents a elevator factory"""

    def __init__(self):
        pass

    @staticmethod
    def build_elevator(number_of_floors, elevator_type):

        if not elevator_type:
            raise ValueError("type is null.")

        if elevator_type and elevator_type not in ["MODEL_A", "MODEL_B"]:
            raise ValueError("Invalid type: ", type)

        if number_of_floors < 0:
            raise ValueError("Number of floors is less than 0")

        if elevator_type == "MODEL_A":
            return ModelAElevator(number_of_floors)

        if elevator_type == "MODEL_B":
            return ModelBElevator(number_of_floors)

        return None

