def find(search_list, value):
    start: int = 0
    end: int = len(search_list) - 1

    while start <= end:
        middle: int = int((end + start) / 2)
        if value == search_list[middle]:
            return middle
        if value < search_list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    raise ValueError("value not in array")
