def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    data: dict[str, int] = {}

    for points in legacy_data:
        for letter in legacy_data[points]:
            data[letter.lower()] = points

    return data
