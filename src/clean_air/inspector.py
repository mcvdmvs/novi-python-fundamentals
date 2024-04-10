from dataclasses import dataclass

"""
Use the dataclass decorator to create a class with a namedtuple-like interface.
https://docs.python.org/3/library/dataclasses.html
"""


@dataclass
class Inspector:
    code: str
    name: str
    location: str
