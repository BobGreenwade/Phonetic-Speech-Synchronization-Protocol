SUPPORTED_VERSION = 0x01

def check_version(version_byte: int) -> bool:
    """Return True if version is supported."""
    return version_byte == SUPPORTED_VERSION

def get_version() -> int:
    """Return current protocol version."""
    return SUPPORTED_VERSION
