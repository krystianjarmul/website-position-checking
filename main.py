import json
from dataclasses import dataclass
from typing import List, Callable, Union


def app(environ: dict, start_response: Callable) -> List[bytes]:
    status = "200 OK"
    headers = [
        ("Content-Type", "application/json; charset=utf-8")
    ]

    start_response(status, headers)

    response_body = get_response_body({"hello": "world"})

    return response_body


def get_response_body(data: dict) -> List[bytes]:
    response = json.dumps(data)
    return [response.encode("utf-8")]


def fizz_buzz(n: int):
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print(i, "fizzbuzz")
        else:
            if i % 3 == 0:
                print(i, "fizz")
            elif i % 5 == 0:
                print(i, "buzz")


def get_rows(arr: Union[List[int]], n: int) -> List[List[int]]:
    return [arr[i:i + n] for i in range(0, len(arr), n)]


def fibb(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fibb(n - 2) + fibb(n - 1)


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return factorial(n - 1) * n


def is_prime(n: int) -> bool:
    count = n // 6
    if not count:
        count = 1

    if n == 1:
        return False
    elif n in [2, 3]:
        return True

    elif n > count * 6:
        return n == count * 6 + 1
    elif n < count * 6:
        return n == count * 6 - 1
    return False


def is_palindrome(text: str) -> bool:
    text = text.lower()
    original_text, reversed_text = text, text[::-1]
    if original_text != reversed_text:
        return False
    return True


data = "Krystian,Jarmul,25,programmer;Maciej,Dyjewski,26,businessman;Sebastian,Jarmul,25,programmer;Marcin,Smolen,23,electrican"


@dataclass
class Person:
    name: str
    age: int
    profession: str


def create_person(record: str) -> Person:
    parts = record.split(",")
    return Person(
        name=" ".join(parts[:2]),
        age=int(parts[2]),
        profession=parts[3]
    )


def to_dicts(people: List[Person]) -> List[dict]:
    return [vars(person) for person in people]


def parse_data(data: str) -> List[dict]:
    records = data.split(";")
    people = [create_person(record) for record in records]
    return to_dicts(people)

from pprint import pprint

pprint(parse_data(data))

if __name__ == '__main__':
    # fizz_buzz(100)
    assert get_rows([1, 2, 3, 4, 5], 3) == [[1, 2, 3], [4, 5]]
    assert fibb(0) == 0
    assert fibb(1) == 1
    assert fibb(2) == 1
    assert fibb(4) == 3
    assert is_palindrome("Anna")
    assert is_palindrome("Kajak")
    assert is_palindrome("Python") is False
    assert is_prime(1) is False
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(4) is False
    assert is_prime(5)
    assert is_prime(51) is False
    assert is_prime(13)
    assert is_prime(19)
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(6) == 720
