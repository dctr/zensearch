import os
import json
from typing import Any, Union
from zensearch.error_handler import handle_errors
from zensearch.asset import Asset


def _get_asset_paths(assets_dir: str) -> list[str]:
    return [
        os.path.join(assets_dir, file_name)
        for file_name in os.listdir(assets_dir)
    ]


def _validate_asset_path(asset_path: str) -> Union[Exception, str]:
    if os.path.isfile(asset_path) and str(asset_path).lower().endswith(
        ".json"
    ):
        return asset_path
    return Exception(f"Invalid asset path {asset_path}")


def _parse_json(asset_path: str) -> Union[Exception, tuple[str, Any]]:
    try:
        with open(asset_path, "r") as file_object:
            file_content = file_object.read()
            asset_object = json.loads(file_content)
            return (asset_path, asset_object)
    except Exception as exception:  # pylint: disable=broad-except
        return Exception(
            f"Unable to process file {asset_path}: {str(exception)}"
        )


def _validate_asset(parsed_asset: tuple[str, Any]) -> Union[Exception, Asset]:
    asset_path, parsed_json = parsed_asset
    if not isinstance(parsed_json, list):
        return Exception(f"Asset did not contain a list {asset_path}")
    if len(parsed_json) == 0:
        return Exception(f"Asset does not contain entries {asset_path}")
    for item in parsed_json:
        if not isinstance(item, dict):
            return Exception(
                f"Asset did not contain a list of objects {asset_path}"
            )
        if not item:
            return Exception(f"Asset contains empty objects {asset_path}")
    return Asset(asset_path, parsed_json)


def load_assets(assets_dir: str) -> list[Asset]:
    asset_paths = _get_asset_paths(assets_dir)
    valid_asset_paths = handle_errors(
        [_validate_asset_path(asset_path) for asset_path in asset_paths]
    )
    parsed_assets = handle_errors(
        [_parse_json(asset_path) for asset_path in valid_asset_paths]
    )
    valid_assets = handle_errors(
        [_validate_asset(parsed_asset) for parsed_asset in parsed_assets]
    )
    return valid_assets
