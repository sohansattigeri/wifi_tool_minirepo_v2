class WiFiError(Exception):
    """Base exception for Wi-Fi related errors."""
    pass

class ConnectionError(WiFiError):
    """Raised when connection fails."""
    pass

class SignalError(WiFiError):
    """Raised when signal information cannot be retrieved."""
    pass
