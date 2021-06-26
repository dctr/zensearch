import os
from zensearch.asset_loader import load_assets
from zensearch.repl import Repl


def main() -> None:
    assets_dir = os.environ.get("ASSETS_DIR", "./zensearch/assets")
    assets = load_assets(assets_dir)
    Repl(assets).run()


if __name__ == "__main__":
    main()
