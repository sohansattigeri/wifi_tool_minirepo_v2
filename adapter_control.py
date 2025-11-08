import subprocess, time

def set_adapter_state(adapter_name: str, enable=True, retries=5) -> bool:
    state = "enable" if enable else "disable"
    subprocess.run(["netsh","interface","set","interface",adapter_name,state],check=False)
    for _ in range(retries):
        out = subprocess.run(["netsh","interface","show","interface",adapter_name],capture_output=True,text=True)
        if enable and "Enabled" in out.stdout: return True
        if not enable and "Disabled" in out.stdout: return True
        time.sleep(0.5)
    return False
