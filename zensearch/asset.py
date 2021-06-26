from pathlib import Path
from typing import Any


class Asset:
    def __init__(self, path: str, asset: list[dict[str, Any]]) -> None:
        self._path = path
        path_stem = Path(path).stem
        self.friendly_name = path_stem.title()
        self._asset = asset
        # Naive heuristic, every item has the same keys.
        # Pre-calculating them for performance reasons.
        # Note: Can't be empty as per asset loader, so asset[0] exists.
        self.keys = asset[0].keys()

    def info(self) -> str:
        return (
            f"Asset {self.friendly_name} has "
            f"{len(self._asset)} entries and {len(self.keys)} keys."
        )

    def search(self, key: str, value: str) -> list[dict[str, Any]]:
        if not key in self.keys:
            return [
                {"error": f"Key '{key}' not found in {self.friendly_name}."}
            ]

        value_type = type(self._asset[0][key])
        if value_type == list:
            return self._search_list(key, value)
        return self._search_for_type(value_type, key, value)

    def _search_list(self, key: str, value: str) -> list[dict[str, Any]]:
        if not value:
            return [item for item in self._asset if len(item[key]) == 0]
        return [item for item in self._asset if value in item[key]]

    def _search_for_type(
        self, value_type: type, key: str, value: str
    ) -> list[dict[str, Any]]:
        query_value: Any
        if value_type == str:
            query_value = value
        elif value_type in [int, float]:
            query_value = value_type(value)
        elif value_type == bool:
            query_value = value.lower() == "true"
        else:
            return [
                {"error": f"Search on type '{value_type}' not implemented."}
            ]
        return [item for item in self._asset if item[key] == query_value]
