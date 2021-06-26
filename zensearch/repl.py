import json
import re
from zensearch.asset import Asset


class Repl:
    def __init__(self, assets: list[Asset]) -> None:
        self._assets = assets

    def run(self) -> None:
        print()
        _welcome()
        print()
        _help()
        print()
        self._repl_loop()

    def _repl_loop(self) -> None:
        command = ""
        while True:
            command = input("command > ").strip()
            if command == "assets":
                print()
                self._handle_assets()
            elif match := re.match(r"^info (\d+)$", command):
                print()
                self._handle_info(int(match.group(1)))
            elif match := re.match(r"^search (\d+)$", command):
                key = input("key > ")
                value = input("value > ")
                print()
                self._handle_search(int(match.group(1)), key, value)
            elif command in ["exit", "quit"]:
                print()
                print("--- Goodbye ---")
                break
            elif command == "help":
                print()
                _help()
            elif command == "":
                pass
            else:
                print()
                _invalid_command(command)
            print()
        print()

    def _handle_assets(self) -> None:
        for index, asset in enumerate(self._assets):
            print(f"{index}) {asset.friendly_name}")

    def _handle_info(self, index: int) -> None:
        if index < len(self._assets):
            print(self._assets[index].info())
            print("Queryable keys:")
            _print_separator()
            print(*list(self._assets[index].keys), sep="\n")
            _print_separator()
        else:
            print("Asset Index out of bounds.")
            self._handle_assets()

    def _handle_search(self, index: int, key: str, value: str) -> None:
        if index < len(self._assets):
            print(
                (
                    f"Searching {self._assets[index].friendly_name} "
                    f"for entries with key {key} and value {value}."
                )
            )
            result = self._assets[index].search(key, value)
            _print_separator()
            print(json.dumps(result, indent=2))
            _print_separator()
        else:
            self._print_out_of_bounds()

    def _print_out_of_bounds(self) -> None:
        print("Asset Index out of bounds.")
        self._handle_assets()


def _welcome() -> None:
    print("Welcome to ZenSearch ℤ🔎")
    print("")
    print("Type 'exit' or 'quit' to exit and 'help' for usage instructions.")


def _help() -> None:
    print("`assets`: Print assets with asset IDs available to be searched.")
    print("`info [n]`: Get information on asset with ID n.")
    print("`search [n]`: Initiate search on asset with ID n.")
    print("`exit` or `quit`: End program.")
    print("`help`: Print this help.")


def _invalid_command(command: str) -> None:
    print("Invalid command", command)
    _help()


def _print_separator() -> None:
    print("--------------------------------------------------")
