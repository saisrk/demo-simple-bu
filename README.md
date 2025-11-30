# Flask App with Bug

A minimal Flask app demonstrating a missing null check bug.

## The Bug

The `/greet` endpoint expects a `name` field in the JSON payload but doesn't validate it exists. When `name` is missing, it raises a `KeyError` instead of returning a proper error response.

**Location**: `app.py`, line 9
```python
name = data['name']  # KeyError if 'name' key is missing
```

## Setup

```bash
pip install flask pytest
```

## Reproduce the Bug

### Run the failing test:
```bash
pytest tests/test_app.py -v
```

The `test_greet_without_name` test will fail because the app returns 500 instead of 400.

### Manual reproduction:
```bash
python app.py
```

Then in another terminal:
```bash
curl -X POST http://localhost:5000/greet \
  -H "Content-Type: application/json" \
  -d '{}'
```

You'll see a 500 error with KeyError traceback.

## Fix

Add a null check:
```python
name = data.get('name')
if not name:
    return jsonify({'error': 'name is required'}), 400
```
