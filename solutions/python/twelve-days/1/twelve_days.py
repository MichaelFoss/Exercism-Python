VERSE_PREFIX: str = "On the [[DAY]] day of Christmas my true love gave to me: "

GIFTS: list[tuple[str, str]] = [
    ("first", "a Partridge in a Pear Tree."),
    ("second", "two Turtle Doves, "),
    ("third", "three French Hens, "),
    ("fourth", "four Calling Birds, "),
    ("fifth", "five Gold Rings, "),
    ("sixth", "six Geese-a-Laying, "),
    ("seventh", "seven Swans-a-Swimming, "),
    ("eighth", "eight Maids-a-Milking, "),
    ("ninth", "nine Ladies Dancing, "),
    ("tenth", "ten Lords-a-Leaping, "),
    ("eleventh", "eleven Pipers Piping, "),
    ("twelfth", "twelve Drummers Drumming, "),
]

def get_verse_prefix(day_num: int) -> str:
    if day_num not in range(1, 13):
        raise ValueError("Verses must be between 1 and 12")
    return "On the [[DAY]] day of Christmas my true love gave to me: ".replace("[[DAY]]", GIFTS[day_num - 1][0])

def recite(start_verse, end_verse):
    lyrics: list[str] = []
    for verse_num in range(start_verse, end_verse + 1):
        verse: str = get_verse_prefix(verse_num)
        for gift_num in range(verse_num, 0, -1):
            if verse_num > 1 and gift_num == 1:
                verse += "and "
            verse += GIFTS[gift_num - 1][1]
        lyrics.append(verse)
    return lyrics
