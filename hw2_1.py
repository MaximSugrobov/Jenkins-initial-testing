from itertools import permutations

# Initial parameters for the clue:
# post_office = ((0, 2),)
# st_grib, st_baker, st_b_sad, st_green = (2, 5), (5, 2), (6, 6), (8, 3)
# address_data = (st_grib, st_baker, st_b_sad, st_green)


class OptimalRoute:

    def __init__(self, possible_route=tuple(), start_point=tuple(), end_point=tuple(), address_data=tuple()):
        self.start_point = start_point
        self.end_point = end_point
        self.address_data = address_data
        self.possible_route = possible_route
        self.route_length = [OptimalRoute.length_calc(possible_route[i], possible_route[i + 1])
                             for i in range(len(possible_route) - 1)]

    def find_all_possible_routes(self):
        routes = []
        for permutation in permutations(self.address_data):
            possible_route = (self.start_point,) + permutation + (self.end_point,)
            routes.append(OptimalRoute(possible_route))
        return routes

    @staticmethod
    def length_calc(point_1, point_2):
        return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5

    def get_optimal_route(self):
        optimal_route = min(self.find_all_possible_routes(),
                            key=lambda route: route.route_length)
        result = str(optimal_route.possible_route[0])
        for i in range(1, len(optimal_route.possible_route)):
            result += f' -> {optimal_route.possible_route[i]}[{sum(optimal_route.route_length[:i])}]'
        result += f' = {sum(optimal_route.route_length)}'
        return result


answer = OptimalRoute(start_point=(0), end_point=(0, 2), address_data=((2, 5), (5, 2), (6, 6), (8, 3)))
print(OptimalRoute.get_optimal_route(answer))

# Testing for another parameters:
another_answer = OptimalRoute(start_point=(1, 1), end_point=(9, 9),
                              address_data=((4, 6), (3, 8), (7, 3), (8, 2), (1, 6), (2, 9)))
print(OptimalRoute.get_optimal_route(another_answer))
