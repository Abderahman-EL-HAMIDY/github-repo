def classify(a, b, c):
    """Bug summary:
    - Incorrect triangle validity check: uses `and` where it should use `or`,
      so many invalid triangles will be marked valid.
    - "isoceles" is misspelled as "isoceles".
    """
    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"

    if a == b == c:
        return "equilateral"

    if a + b <= c and a + c <= b and b + c <= a:  # BUG
        return "invalid"

    if a == b or b == c or a == c:  # BUG spelling
        return "isoceles"

    return "scalene"
