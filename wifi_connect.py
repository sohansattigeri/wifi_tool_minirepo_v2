import subprocess
import time
from .utils import log_info, log_error

def connect_to_wifi(ssid: str, password: str) -> bool:
    """Connect to a Wi-Fi network using Windows netsh command."""
    try:
        log_info(f"Attempting to connect to '{ssid}'...")
        profile_name = ssid

        # Check if profile exists
        profile_check = subprocess.run(
            ["netsh", "wlan", "show", "profiles"],
            capture_output=True, text=True
        )

        if ssid not in profile_check.stdout:
            # Create a temporary XML profile if not present
            profile_xml = f"""
            <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
                <name>{ssid}</name>
                <SSIDConfig>
                    <SSID>
                        <name>{ssid}</name>
                    </SSID>
                </SSIDConfig>
                <connectionType>ESS</connectionType>
                <connectionMode>auto</connectionMode>
                <MSM>
                    <security>
                        <authEncryption>
                            <authentication>WPA2PSK</authentication>
                            <encryption>AES</encryption>
                            <useOneX>false</useOneX>
                        </authEncryption>
                        <sharedKey>
                            <keyType>passPhrase</keyType>
                            <protected>false</protected>
                            <keyMaterial>{password}</keyMaterial>
                        </sharedKey>
                    </security>
                </MSM>
            </WLANProfile>
            """
            xml_file = f"{ssid}.xml"
            with open(xml_file, "w") as f:
                f.write(profile_xml)
            subprocess.run(["netsh", "wlan", "add", "profile", f"filename={xml_file}"], check=True)

        # Try connecting
        result = subprocess.run(
            ["netsh", "wlan", "connect", f"name={profile_name}"],
            capture_output=True, text=True
        )

        time.sleep(3)
        if "successfully" in result.stdout.lower():
            log_info(f"✅ Connected successfully to '{ssid}'")
            return True
        else:
            log_error(f"❌ Connection failed: {result.stderr or result.stdout}")
            return False

    except Exception as e:
        log_error(f"Exception during Wi-Fi connection: {e}")
        return False


def disconnect_wifi():
    """Disconnect from current Wi-Fi network."""
    try:
        result = subprocess.run(["netsh", "wlan", "disconnect"], capture_output=True, text=True)
        if "successfully" in result.stdout.lower():
            log_info(" Disconnected from Wi-Fi")
        else:
            log_error("⚠️ Failed to disconnect (may not be connected).")
    except Exception as e:
        log_error(f"Exception during disconnect: {e}")
