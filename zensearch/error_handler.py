from typing import Any, Union


def handle_errors(elements: list[Union[Exception, Any]]) -> list[Any]:
    result = []
    for element in elements:
        if isinstance(element, Exception):
            print("[ERROR]", repr(element))
        else:
            result.append(element)
    return result
