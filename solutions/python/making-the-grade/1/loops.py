"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores) -> list[int]:
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    int_scores = []
    for score in student_scores:
        int_scores.append(round(score))
    return int_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    PASSING_GRADE = 41
    failing_student_count = 0
    for score in student_scores:
        if score < PASSING_GRADE:
            failing_student_count += 1
    return failing_student_count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    best_scores: list[int] = []
    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)
    return best_scores


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    grade_increment_step: float = round(100 - highest) / 4
    passing_grades: list[int] = []
    BASE_PASSING_GRADES: list[int] = [41, 56, 71, 86]
    for base_passing_grade_index, base_passing_grade in enumerate(BASE_PASSING_GRADES):
        passing_grades.append(int(base_passing_grade - grade_increment_step * base_passing_grade_index))
    return passing_grades


def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    if len(student_scores) != len(student_names):
        raise ValueError('Student scores and names must have identical length')

    ranking: list[str] = []
    for index, _ in enumerate(student_scores):
        ranking.append(f'{index + 1}. {student_names[index]}: {student_scores[index]}')
    return ranking


def perfect_score(student_info: list[list]) -> list:
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    PERFECT_SCORE = 100

    for student_data in student_info:
        if len(student_data) != 2:
            raise ValueError('Each student must have a name and a score')
        if student_data[1] == PERFECT_SCORE:
            return student_data

    return []