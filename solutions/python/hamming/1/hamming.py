VALID_DNA = 'GATC'

def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    distance: int = 0
    for index in range(0, len(strand_a)):
        if (strand_a[index] not in VALID_DNA or
            strand_b[index] not in VALID_DNA):
            raise ValueError("Strands must only contain 'GATC'")
        if strand_a[index] != strand_b[index]:
            distance += 1
    return distance