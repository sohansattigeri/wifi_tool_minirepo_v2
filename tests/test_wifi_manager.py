import subprocess, pytest
from wifi_manager import WifiManager

class DummyCompleted:
    def __init__(self, stdout): self.stdout, self.returncode = stdout, 0

def fake_run(cmd, capture_output=False, text=False, check=False):
    if "show" in cmd and "interfaces" in cmd:
        return DummyCompleted("Name : Wi-Fi\nState : connected\nSSID : TEST_SSID\n")
    return DummyCompleted("")

@pytest.fixture(autouse=True)
def patch_run(monkeypatch):
    monkeypatch.setattr(subprocess, "run", fake_run)

def test_is_connected_true():
    wm = WifiManager()
    assert wm.is_connected("TEST_SSID")

def test_connect_true():
    wm = WifiManager()
    assert wm.connect("TEST_SSID", timeout=2)
