import random
from typing import List, Dict


class Utils:

    @staticmethod
    def fetch_closest_candy(data: List, head: Dict):
        candies = data
        closest_candy = {}
        closest_distance = None

        for candy in candies:
            distance = Utils.get_distance(head, candy)
            if closest_distance is None or closest_distance > distance:
                closest_distance = distance
                closest_candy = candy

        return closest_candy

    @staticmethod
    def get_distance(point_a: Dict, point_b: Dict):
        """

        :param point_a:
        :param point_b:
        :return: The number of cases to go through to reach one point starting from the other
        """
        x_distance = abs(point_a["x"]-point_b["x"])
        y_distance = abs(point_a["y"]-point_b["y"])
        return x_distance + y_distance

    @staticmethod
    def get_next_move(head: Dict, target: Dict):

        if head["x"] < target["x"]:
            return "right"
        elif head["x"] > target["x"]:
            return "left"
        elif head["y"] < target["y"]:
            return "down"
        elif head["y"] > target["y"]:
            return "up"
        else:
            directions = ['up', 'down', 'left', 'right']
            return random.choice(directions)

    @staticmethod
    def get_next_move2(body: List, target: Dict):
        head = body[0]
        body_no_tail = body[1:len(body)-1]

        if head["x"] != target["x"]:
            # Check for fastest x move
            fast_x = Utils.get_fast_x(head, target, body_no_tail)
            if fast_x:
                return fast_x
            # If we can't go there check for fastest y move
            fast_y = Utils.get_fast_y(head, target, body_no_tail)
            if fast_y:
                return fast_y
            # If we can't go there check for slowest x move
            slow_x = Utils.get_slow_x(head, target, body_no_tail)
            if slow_x:
                return slow_x
            # If we can't go there go slowest y move
            slow_y = Utils.get_slow_y(head, target, body_no_tail)
            if slow_y:
                return slow_y

        else:
            # If we can't go there check for fastest y move
            fast_y = Utils.get_fast_y(head, target, body_no_tail)
            if fast_y:
                return fast_y

            # If we can't go there go slowest y move
            slow_y = Utils.get_slow_y(head, target, body_no_tail)
            if slow_y:
                return slow_y

            # Check for fastest x move
            fast_x = Utils.get_fast_x(head, target, body_no_tail)
            if fast_x:
                return fast_x

            # If we can't go there check for slowest x move
            slow_x = Utils.get_slow_x(head, target, body_no_tail)
            if slow_x:
                return slow_x


        directions = ['up', 'down', 'left', 'right']
        return random.choice(directions)

    @staticmethod
    def get_fast_x(head: Dict, target: Dict, body_no_tail: List[Dict]):
        x_direction = {1: "right", -1: "left"}

        fast_x = 1 if head["x"] < target["x"] else -1
        if Utils.is_cell_available({"x": head["x"] + fast_x, "y": head["y"]}, body_no_tail):
            return x_direction[fast_x]
        return None

    @staticmethod
    def get_slow_x(head: Dict, target: Dict, body_no_tail: List[Dict]):
        x_direction = {1: "right", -1: "left"}

        fast_x = 1 if head["x"] > target["x"] else -1
        if Utils.is_cell_available({"x": head["x"] + fast_x, "y": head["y"]}, body_no_tail):
            return x_direction[fast_x]
        return None

    @staticmethod
    def get_fast_y(head: Dict, target: Dict, body_no_tail: List[Dict]):
        y_direction = {1: "down", -1: "up"}
        fast_y = 1 if head["y"] < target["y"] else -1
        if Utils.is_cell_available({"x": head["x"], "y": head["y"]+fast_y}, body_no_tail):
            return y_direction[fast_y]
        return None

    @staticmethod
    def get_slow_y(head: Dict, target: Dict, body_no_tail: List[Dict]):
        y_direction = {1: "down", -1: "up"}
        fast_y = 1 if head["y"] > target["y"] else -1
        if Utils.is_cell_available({"x": head["x"], "y": head["y"]+fast_y}, body_no_tail):
            return y_direction[fast_y]
        return None

    @staticmethod
    def is_cell_available(cell: Dict, body: List[Dict]):
        for bit in body:
            if bit["x"] == cell["x"] and bit["y"] == cell["y"]:
                return False
        return True
