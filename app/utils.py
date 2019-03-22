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
