"""A tiny shopping agent.

An AI agent repeats this loop:
  1. Ask the "model" what to do next.
  2. If the model asks for a tool, run the tool and show it the result.
  3. If the model gives a final answer, stop.

Right now the "model" is a simple rule-based stand-in (fake_model), so the
project runs with no internet and no API key. Later, we replace fake_model
with a real AI model and keep everything else the same.
"""
import re

from tools import search_products, get_product

# The tools the agent is allowed to use, by name.
TOOLS = {
    "search_products": search_products,
    "get_product": get_product,
}

STOP_WORDS = {"i", "need", "want", "a", "an", "the", "under", "below", "for", "me", "find", "buy", "some", "rs", "rupees", "please"}


def fake_model(user_request, history):
    """Pretend AI model: decides the next step from the request and history."""
    # Step 1: nothing has been searched yet, so ask for the search tool.
    if not history:
        price_match = re.search(r"(\d+)", user_request)
        max_price = int(price_match.group(1)) if price_match else None
        words = re.findall(r"[a-zA-Z]+", user_request.lower())
        query = " ".join(w for w in words if w not in STOP_WORDS)
        return {"tool": "search_products", "args": {"query": query, "max_price": max_price}}

    # Step 2: we have search results, so write the final answer.
    results = history[-1]["result"]
    if not results:
        return {"final": "Sorry, I could not find a matching product."}
    best = results[0]
    return {"final": f"I recommend the {best['name']} for Rs {best['price']}."}


def run_agent(user_request, model=fake_model, max_steps=5):
    """Run the agent loop and return the final answer as text."""
    history = []
    for _ in range(max_steps):
        decision = model(user_request, history)
        if "final" in decision:
            return decision["final"]
        tool = TOOLS[decision["tool"]]
        result = tool(**decision["args"])
        history.append({"tool": decision["tool"], "args": decision["args"], "result": result})
    return "Sorry, I could not finish the task."


if __name__ == "__main__":
    request = input("What are you looking for? ")
    print(run_agent(request))
