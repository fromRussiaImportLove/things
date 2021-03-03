from datetime import datetime
 
 
def to_python_value(value: str) -> datetime:
    python_iso_format: str = value.replace("Z", "+00:00")
    return datetime.fromisoformat(python_iso_format)
 
 
def to_json_value(value: datetime) -> str:
    python_iso_format: str = value.isoformat()
    return python_iso_format.replace("+00:00", "Z")
 
 
js_value = "2021-03-03T12:31:49.734Z"
dt = to_python_value(js_value)
print(f"JS: {js_value}")
print(f"Python: {dt}")
print(f"Python: {dt.tzinfo}")
print(f"JS: {to_json_value(dt)}")
