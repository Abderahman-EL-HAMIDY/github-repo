def classify(a, b, c):
    """Bug summary:
    - Missing positive-length check.
    - Wrong triangle inequality (uses < instead of <=).
    - Returns numeric code for some cases.
    """
    # BUG: missing non-positive check

    if not (a + b < c and a + c < b and b + c < a):  # BUG wrong logic
        return 0  # BUG returns number

    if a == b == c:
        return "equilateral"

    if a == b or b == c or a == c:
        return "isosceles"

    return "scalene"
