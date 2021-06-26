from zensearch.asset_loader import load_assets

prod_assets = load_assets("./zensearch/assets")
org_assets = [
    asset for asset in prod_assets if asset.friendly_name == "Organizations"
][0]
tickets_assets = [
    asset for asset in prod_assets if asset.friendly_name == "Tickets"
][0]
users_assets = [
    asset for asset in prod_assets if asset.friendly_name == "Users"
][0]


def test_error_org() -> None:
    actual = org_assets.search("nosuchkey", "doesnotmatter")
    assert len(actual) == 1
    assert actual[0]["error"]


def test_int_org() -> None:
    actual = org_assets.search("_id", "101")
    assert len(actual) == 1
    assert actual[0]["_id"] == 101


def test_str_org() -> None:
    actual = org_assets.search("name", "Enthaze")
    assert len(actual) == 1
    assert actual[0]["_id"] == 101


def test_non_ascii_str_org() -> None:
    actual = org_assets.search("details", "MegaCörp")
    assert len(actual) == 3
    assert {item["_id"] for item in actual} == {107, 104, 113}


def test_bool_org() -> None:
    actual = org_assets.search("shared_tickets", "true")
    assert len(actual) == 10


def test_date_org() -> None:
    actual = org_assets.search("created_at", "2016-07-26T09:35:57 -10:00")
    assert len(actual) == 1
    assert actual[0]["_id"] == 108


def test_list_org() -> None:
    actual = org_assets.search("domain_names", "enomen.com")
    assert len(actual) == 1
    assert actual[0]["_id"] == 111


def test_int_tickets() -> None:
    actual = tickets_assets.search("submitter_id", "39")
    assert len(actual) == 3


def test_str_tickets() -> None:
    actual = tickets_assets.search(
        "_id", "436bf9b0-1147-4c0a-8439-6f79833bff5b"
    )
    assert len(actual) == 1
    assert actual[0]["_id"] == "436bf9b0-1147-4c0a-8439-6f79833bff5b"


def test_bool_tickets() -> None:
    actual = tickets_assets.search("has_incidents", "true")
    assert len(actual) == 99


def test_date_tickets() -> None:
    actual = tickets_assets.search("created_at", "2016-01-11T08:56:20 -11:00")
    assert len(actual) == 1
    assert actual[0]["_id"] == "25c518a8-4bd9-435a-9442-db4202ec1da4"


def test_list_tickets() -> None:
    actual = tickets_assets.search("tags", "Utah")
    assert len(actual) == 14


def test_empty_list_users() -> None:
    actual = users_assets.search("tags", "")
    assert len(actual) == 1
    assert actual[0]["_id"] == 99


def test_empty_str_users() -> None:
    actual = users_assets.search("phone", "")
    assert len(actual) == 1
    assert actual[0]["_id"] == 99
