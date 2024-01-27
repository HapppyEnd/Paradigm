"""Binary search."""


def binary_search(number_list: list, element: int) -> int:
    """Binary search."""
    right: int = len(number_list)
    left: int = 0
    while right > left:
        mid = (left + right) // 2
        if number_list[mid] == element:
            return mid
        if number_list[mid] < element:
            left = mid + 1
        else:
            right = mid
    return -1
