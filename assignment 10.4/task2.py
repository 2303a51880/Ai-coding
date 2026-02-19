from collections import Counter


def find_duplicates(data):
    """Return a list of values that appear more than once in `data`.

    The returned list preserves the order of first occurrence in `data`.
    Time complexity: O(n), Space complexity: O(n).
    """
    counts = Counter(data)
    duplicates = []
    seen = set()
    for x in data:
        if counts[x] > 1 and x not in seen:
            duplicates.append(x)
            seen.add(x)
    return duplicates


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]
    print(find_duplicates(numbers))
