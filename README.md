# WiFi Automation Mini Repo (Interview Demo)

This is a minimal example repo for a WiFi Automation Framework used in validation and diagnosis testing.

Includes:
- `wifi_manager.py` : WiFi connection manager
- `adapter_control.py` : enable/disable adapter
- `auto_diagnose.py` : runs diagnostics
- `utils.py` : lightweight logger
- `tests/test_wifi_manager.py` : unit tests using pytest

Run tests:
```bash
pip install -r requirements.txt
pytest -q
```
