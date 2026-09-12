def high_score(score):
    
    try:
        with open("high_score.txt", "r") as f:
            high_score = int(f.read())

    except FileNotFoundError:
        high_score: int = -1

    if score > high_score:
        with open("high_score.txt", "w") as f:
            f.write(str(score))
            high_score = score

    return high_score
