__author__ = 'Cornelius Jemison <cornelius.jemison[@]gmail.com>'

class InstructionSet(object):
    """This class represents a single row in a file"""

    def __init__(self, line):
        self._current_floor = 0
        self._calls = list()
        self._parse_line(line)

    @property
    def current_floor(self):
        return self._current_floor


    @property
    def calls(self):
        return self._calls

    def _parse_line(self, line):
        if line:
            current_floor, iterations = line.split(":")
            if current_floor and iterations:
                self._current_floor = int(current_floor)
                for item in iterations.split(","):
                    x, y = item.split("-")
                    i = Instruction(int(x), int(y))
                    self._calls.append(i)


class Instruction(object):
    """This class represents an instruction set"""

    def __init__(self, start_position=0, end_position=0):
        self._start_position = start_position
        self._end_position = end_position

    @property
    def start_position(self):
        return self._start_position

    @property
    def end_position(self):
        return self._end_position

    @start_position.setter
    def start_position(self, start_position):
        if start_position:
            self._start_position = start_position

    @end_position.setter
    def end_position(self, end_position):
        if end_position:
            self._end_position = end_position

    def validate_instruction(self, number_of_floors):

        if not number_of_floors:
            raise ValueError("number_of_floors is null.")

        if number_of_floors < 1:
            raise ValueError("number_of_floors is less than zero.")

        if not self._start_position:
            raise ValueError("start position number is None.")

        if not self._end_position:
            raise ValueError("end position is None.")

        if self._start_position < 1:
            raise ValueError("start position is less than 1.")

        if self._end_position < 1:
            raise ValueError("end position is less than 1.")

        if self._start_position > number_of_floors:
            raise ValueError("start position is greater than number of floors.")

        if self._end_position > number_of_floors:
            raise ValueError("end position is greater than number of floors.")

        if self._start_position == self._end_position:
            raise ValueError("start position == end position")

    def __repr__(self):
        return "<Instruction %d | %d>" % (self._start_position, self._end_position, )

    def __str__(self):
        return "<Instruction %d | %d>" % (self._start_position, self._end_position, )

    def __hash__(self):
        return hash(self._start_position) ^ hash(self._end_position)

    def __eq__(self, other):
        return self._start_position == other.start_position and self._end_position == other.end_position