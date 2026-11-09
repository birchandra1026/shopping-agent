"""Tools: small, simple functions that an AI agent is allowed to call."""
import json
from pathlib import Path

PRODUCTS_FILE = Path(__file__).parent / "products.json"


def load_products():
    """Read all products from the JSON file."""
    with open(PRODUCTS_FILE, encoding="utf-8") as f:
        return json.load(f)


def search_products(query, max_price=None):
    """Find products whose name or tags contain a word from the query.

    Optionally keep only products that cost max_price or less.
    Results are sorted from cheapest to most expensive.
    """
    words = query.lower().split()
    results = []
    for product in load_products():
        text = (product["name"] + " " + " ".join(product["tags"])).lower()
        matches_word = any(word in text for word in words)
        within_budget = max_price is None or product["price"] <= max_price
        if matches_word and within_budget:
            results.append(product)
    return sorted(results, key=lambda p: p["price"])


def get_product(product_id):
    """Return one product by its id, or None if it does not exist."""
    for product in load_products():
        if product["id"] == product_id:
            return product
    return None
