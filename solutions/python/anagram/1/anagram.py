def get_sorted_letters(word: str) -> list[str]:
    letters: list[str] = list(word.lower())
    letters.sort()
    return letters

def is_anagram(sorted_word_letters: list[str], potential_anagram: str) -> bool:
    potential_anagram_letters = get_sorted_letters(potential_anagram)
    return potential_anagram_letters == sorted_word_letters

def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    word = word.lower()
    anagrams: list[str] = []
    sorted_word_letters: list[str] = get_sorted_letters(word)
    for candidate in candidates:
        candidate_is_identical: bool = candidate.lower() == word
        if candidate_is_identical:
            continue
        if is_anagram(sorted_word_letters, candidate):
            anagrams.append(candidate)
    return anagrams
