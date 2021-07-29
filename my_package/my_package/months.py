from typing import List

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

def cycle_months(loi: List[int]) -> List[str]:
    """
    Returns a list of a months corresponding the months that correspond
    to the index numbers in `loi`, modulo 12.
    
    All indexes are zero-indexed.
    """
    acc = []
    for idx in loi:
        acc.append(MONTHS[idx % 12])
    return acc
