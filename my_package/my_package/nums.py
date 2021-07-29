from typing import List

from dataclasses import dataclass

@dataclass
class MyClass:
    data: str
        
# Interp. An example class with generic data
        
MC1 = MyClass("Some Data")

def create_number_sequence(n: int) -> List[int]:
    """
    Returns a list of consecutive numbers starting from 0 and ending with 'n'.
    """
    return list(range(n + 1)) # Built-in function range() generates consecutive numbers
