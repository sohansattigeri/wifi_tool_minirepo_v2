from wifi_manager import WifiManager
from adapter_control import set_adapter_state
import json

def collect_logs():
    return {"logs": ["WiFi diagnostic sample log."]}

def run_auto_diagnose(target_ssid: str):
    wm = WifiManager()
    report = {"adapter": wm.adapter}
    connected = wm.connect(target_ssid, timeout=10)
    report["connected"] = connected
    if not connected:
        set_adapter_state(wm.adapter, enable=False)
        set_adapter_state(wm.adapter, enable=True)
        connected_retry = wm.connect(target_ssid, timeout=8)
        report["connected_after_retry"] = connected_retry
    else:
        report["connected_after_retry"] = True
    report["logs"] = collect_logs()
    return report

if __name__ == "__main__":
    print(json.dumps(run_auto_diagnose("Test_SSID"), indent=2))
