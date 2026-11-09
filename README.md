# Shopping Agent (starter project)

A small Python project that shows how an AI agent works: a loop where a
"model" decides what to do, calls tools (functions), reads the results and
gives a final answer.

## Files
- `products.json` - the product data (8 sample products)
- `tools.py` - functions the agent can call (`search_products`, `get_product`)
- `agent.py` - the agent loop; `fake_model` is a rule-based stand-in for a real AI model
- `test_tools.py`, `test_agent.py` - automated tests (pytest)

## Run it
```
python agent.py
```
Example: type `I need gym stuff under 700`.

## Run the tests
```
pip install -r requirements.txt
pytest
```

## Next steps
- [ ] Replace `fake_model` with a real AI model
- [ ] Add more tools (for example `add_to_cart`)
- [ ] Add more tests
