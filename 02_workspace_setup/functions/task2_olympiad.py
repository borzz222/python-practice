"""Определитель наличия места по баллам за олимпиаду в тройке победителей."""


def check_winners(scores, student_score):
    """Печатает, вошёл ли участник в тройку победителей.

    Args:
        scores: список баллов всех участников.
        student_score: количество набранных участником баллов.
    """
    done_scores = sorted(scores, reverse=True)
    if student_score in done_scores[:3]:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")


if __name__ == "__main__":
    all_scores = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]
    check_winners(all_scores, 51)  # должно быть: Вы в тройке победителей!
    check_winners(all_scores, 41)  # должно быть: Вы не попали в тройку победителей.