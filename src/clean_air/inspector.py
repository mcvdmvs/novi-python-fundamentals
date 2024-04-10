from dataclasses import dataclass


@dataclass
class Inspector:
    code: str
    name: str
    location: str
