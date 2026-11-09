from agent import run_agent


def test_agent_recommends_cheapest_matching_product():
    answer = run_agent("I need gym stuff under 700")
    assert "Steel Water Bottle" in answer


def test_agent_handles_no_results():
    answer = run_agent("I want a spaceship")
    assert "could not find" in answer


def test_agent_stops_if_model_never_finishes():
    def stubborn_model(request, history):
        return {"tool": "get_product", "args": {"product_id": 1}}

    assert run_agent("anything", model=stubborn_model, max_steps=3).startswith("Sorry")
