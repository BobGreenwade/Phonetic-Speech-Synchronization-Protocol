from functools import reduce

VERSION = 0x01

def compute_checksum(data: bytes) -> int:
    """Compute XOR checksum of all bytes."""
    return reduce(lambda x, y: x ^ y, data)

def add_header(flag: int, payload: bytes) -> bytes:
    """Prepend flag and version, then append checksum."""
    packet = bytearray()
    packet.append(flag)
    packet.append(VERSION)
    packet.extend(payload)
    packet.append(compute_checksum(packet))
    return bytes(packet)

def verify_checksum(packet: bytes) -> bool:
    """Verify checksum matches XOR of all previous bytes."""
    return compute_checksum(packet[:-1]) == packet[-1]
