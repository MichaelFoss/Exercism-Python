import re

"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons: int) -> list[int]:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return [*wagons]


def fix_list_of_wagons(each_wagons_id: list[int], missing_wagons: list[int]) -> list[int]:
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """

    [first, second, primary, *rest] = each_wagons_id
    first: int
    second: int
    primary: int
    rest: list[int]
    return [primary, *missing_wagons, *rest, first, second]


def add_missing_stops(route: dict, *stops: str, **kwstops: dict[str, str]) -> dict:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    if "stops" not in route:
        route["stops"] = []
    if stops != None and len(stops) > 0:
        route["stops"] = route["stops"] + stops
    if kwstops != None and len(kwstops) > 0:
        kws: list[str] = kwstops.keys()
        sorted_stops: list[dict] = []
        for (key_index, key) in enumerate(kws):
            if not key.startswith('stop_'):
                raise ValueError(f"Stop '{key}' must start with 'stop_'")
            stripped_key = key[len('stop_'):]
            if not re.search(r'^\d+$', stripped_key):
                raise ValueError(f"Stop '{stripped_key}' must be numeric")
            stop_num: int = int(stripped_key)
            sorted_stops.append({
                "stop_num": stop_num,
                "key": key,
                "stop": kwstops[key],
            })
        sorted_stops.sort(key = lambda x: x["stop_num"])
        for sorted_stop in sorted_stops:
            route["stops"].append(sorted_stop["stop"])
    return route

def extend_route_information(route: dict, more_route_information: dict) -> dict:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    new_route: dict = {}
    for (key, val) in route.items():
        new_route[key] = val
    for (key, val) in more_route_information.items():
        new_route[key] = val
    return new_route


def fix_wagon_depot(wagons_rows: list[list[tuple[int, str]]]) -> list[list[tuple[int, str]]]:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    if len(wagons_rows) == 0:
        return []
    fixed_wagons_rows: list[list[tuple[int, str]]] = list([] for _ in range(len(wagons_rows[0])))
    for row in wagons_rows:
        for (col_index, cell) in enumerate(row):
            fixed_wagons_rows[col_index].append(cell)
    return fixed_wagons_rows
