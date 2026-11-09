from tools import search_products, get_product


def test_search_finds_matching_product():
    results = search_products("shoes")
    assert results[0]["name"] == "Running Shoes"


def test_search_respects_max_price():
    results = search_products("gym", max_price=600)
    assert [p["name"] for p in results] == ["Steel Water Bottle"]


def test_search_with_no_match_returns_empty_list():
    assert search_products("spaceship") == []


def test_get_product_returns_correct_item():
    assert get_product(3)["name"] == "Leather Wallet"


def test_get_product_unknown_id_returns_none():
    assert get_product(999) is None
