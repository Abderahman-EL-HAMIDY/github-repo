def classify(a, b, c):
    """Bug summary:
    - Converts numbers to strings and uses lexicographic comparisons.
    - Breaks triangle inequality for multi-digit numbers.
    """
    sa, sb, sc = str(a), str(b), str(c)  # BUG

    if sa == sb == sc:
        return "equilateral"

    sides = sorted([sa, sb, sc])  # BUG lexicographic sorting

    if not (sides[0] + sides[1] > sides[2]):  # BUG string comparison
        return "invalid"

    if sa == sb or sb == sc or sa == sc:  # string-based equality
        return "isosceles"

    return "scalene"
