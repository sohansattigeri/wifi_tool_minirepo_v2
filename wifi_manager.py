import subprocess, time

def parse_adapter_name(output: str) -> str:
    for line in output.splitlines():
        if line.strip().startswith("Name"):
            return line.split(":",1)[1].strip()
    return "Wi-Fi"

class WifiManager:
    def __init__(self, adapter_name=None):
        self.adapter = adapter_name or self._detect_adapter()

    def _detect_adapter(self):
        try:
            out = subprocess.run(["netsh","wlan","show","interfaces"],capture_output=True,text=True)
            return parse_adapter_name(out.stdout)
        except Exception:
            return "Wi-Fi"

    def is_connected(self, ssid: str) -> bool:
        try:
            out = subprocess.run(["netsh","wlan","show","interfaces"],capture_output=True,text=True)
            return ssid in out.stdout and "State" in out.stdout
        except Exception:
            return False

    def connect(self, ssid: str, timeout=15) -> bool:
        subprocess.run(["netsh","wlan","connect",f"name={ssid}"],check=False)
        start = time.time()
        while time.time()-start < timeout:
            if self.is_connected(ssid):
                return True
            time.sleep(1)
        return False
