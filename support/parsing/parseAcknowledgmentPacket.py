"""
parseAcknowledgmentPacket.py

Parses an Acknowledgment Packet from the PSSP protocol.

Drafted and created by Bob Greenwade, ChatGPT-4o, and Copilot.
"""

from support.packet_utils import verify_checksum
from support.versioning import check_version

def parse_acknowledgment_packet(packet: bytes) -> dict:
    """
    Parse an Acknowledgment Packet.

    Parameters:
        packet (bytes): Raw packet bytes

    Returns:
        dict: Parsed fields including sentence length

    Raises:
        ValueError: If packet is invalid or checksum fails
    """

    if len(packet) < 7:
        raise ValueError("Packet too short for acknowledgment")

    flag = packet[0]
    version = packet[1]
    length = int.from_bytes(packet[2:4], 'little')
    code = packet[4:6]
    checksum = packet[-1]

    if flag != 0x04:
        raise ValueError("Incorrect packet flag for acknowledgment")
    if not check_version(version):
        raise ValueError("Unsupported protocol version")
    if code != b'\x1B\x1B':
        raise ValueError("Invalid acknowledgment code")
    if not verify_checksum(packet):
        raise ValueError("Checksum mismatch")

    return {
        "flag": flag,
        "version": version,
        "length": length,
        "code": code.hex(),
        "valid": True
    }
