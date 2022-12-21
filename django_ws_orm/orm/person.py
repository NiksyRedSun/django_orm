from dataclasses import dataclass


@dataclass()
class Person:
    id: int = None
    name: str = None
    age:  int = None