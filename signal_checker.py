import random

def is_signal_strong(threshold: int = 60) -> bool:
    """Simulate checking WiFi signal strength."""
    strength = random.randint(30, 100)
    print(f" Current signal strength: {strength}%")
    return strength >= threshold
    if strength >= threshold:
        print(" Signal is strong.")
        return True
    else:
        print(" Signal is weak.")
        return False    