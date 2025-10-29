"""
parseVolumePacket.py

Parses a Volume Packet from the PSSP protocol.

Drafted and created by Bob Greenwade, ChatGPT-4o, and Copilot.
"""

from support.packet_utils import verify_checksum
from support.versioning import check_version

def parse_volume_packet(packet: bytes) -> dict:
    """
    Parse a Volume Packet.

    Parameters:
        packet (bytes): Raw packet bytes

    Returns:
        dict: Parsed fields including volume level and optional explanation

    Raises:
        ValueError: If packet is invalid or checksum fails
    """

    if len(packet) < 4:
        raise ValueError("Packet too short for volume")

    flag = packet[0]
    version = packet[1]
    volume = packet[2]
    length = packet[3]

    expected_len = 4 + length + 1
    if len(packet) != expected_len:
        raise ValueError("Packet length mismatch")
    if flag != 0x05:
        raise ValueError("Incorrect packet flag for volume")
    if not check_version(version):
        raise ValueError("Unsupported protocol version")
    if not verify_checksum(packet):
        raise ValueError("Checksum mismatch")

    explanation = packet[4:4+length].decode('utf-8')

    return {
        "flag": flag,
        "version": version,
        "volume": volume,
        "explanation": explanation,
        "valid": True
    }
