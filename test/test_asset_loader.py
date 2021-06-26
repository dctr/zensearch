from zensearch.asset import Asset
from zensearch.asset_loader import (
    _validate_asset_path,
    _parse_json,
    _validate_asset,
)


def test_not_a_file() -> None:
    actual = _validate_asset_path("/does/not/exist")
    assert isinstance(actual, Exception)


def test_not_a_json_txt() -> None:
    actual = _validate_asset_path("./test/assets/foo.txt")
    assert isinstance(actual, Exception)


def test_not_a_json_dir() -> None:
    actual = _validate_asset_path("./test/assets/bar.json")
    assert isinstance(actual, Exception)


def test_valid_json_path() -> None:
    actual = _validate_asset_path("./test/assets/valid-asset.json")
    assert isinstance(actual, str)


def test_invalid_json_file() -> None:
    actual = _parse_json("./test/assets/invalid-json.json")
    assert isinstance(actual, Exception)


def test_nonexisting_json_file() -> None:
    actual = _parse_json("/does/not/exist")
    assert isinstance(actual, Exception)


def test_valid_json_file() -> None:
    actual = _parse_json("./test/assets/valid-asset.json")
    assert not isinstance(actual, Exception)


def test_invalid_asset_1() -> None:
    parsed_json = _parse_json("./test/assets/invalid-asset-1.json")
    assert not isinstance(parsed_json, Exception)
    actual = _validate_asset(parsed_json)
    assert isinstance(actual, Exception)


def test_invalid_asset_2() -> None:
    parsed_json = _parse_json("./test/assets/invalid-asset-2.json")
    assert not isinstance(parsed_json, Exception)
    actual = _validate_asset(parsed_json)
    assert isinstance(actual, Exception)


def test_invalid_asset_3() -> None:
    parsed_json = _parse_json("./test/assets/invalid-asset-3.json")
    assert not isinstance(parsed_json, Exception)
    actual = _validate_asset(parsed_json)
    assert isinstance(actual, Exception)


def test_invalid_asset_4() -> None:
    parsed_json = _parse_json("./test/assets/invalid-asset-4.json")
    assert not isinstance(parsed_json, Exception)
    actual = _validate_asset(parsed_json)
    assert isinstance(actual, Exception)


def test_invalid_asset_5() -> None:
    parsed_json = _parse_json("./test/assets/invalid-asset-5.json")
    assert not isinstance(parsed_json, Exception)
    actual = _validate_asset(parsed_json)
    assert isinstance(actual, Exception)


def test_valid_asset() -> None:
    parsed_json = _parse_json("./test/assets/valid-asset.json")
    assert not isinstance(parsed_json, Exception)
    actual = _validate_asset(parsed_json)
    assert isinstance(actual, Asset)
