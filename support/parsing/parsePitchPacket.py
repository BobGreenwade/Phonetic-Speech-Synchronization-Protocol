"""
parsePitchPacket.py

Parses a Pitch Packet from the PSSP protocol.

Drafted and created by Bob Greenwade, ChatGPT-4o, and Copilot.
"""

from support.packet_utils import verify_checksum
from support.versioning import check_version

def parse_pitch_packet(packet: bytes) -> dict:
    """
    Parse a Pitch Packet.

    Parameters:
        packet (bytes): Raw packet bytes

    Returns:
        dict: Parsed fields including tone, pitch, slide duration, and explanation

    Raises:
        ValueError: If packet is invalid or checksum fails
    """

    if len(packet) < 8:
        raise ValueError("Packet too short for pitch")

    flag = packet[0]
    version = packet[1]
    tone = packet[2]
    pitch = packet[3]
    slide_ms = int.from_bytes(packet[4:8], 'little')
    length = packet[8]

    expected_len = 9 + length + 1
    if len(packet) != expected_len:
        raise ValueError("Packet length mismatch")
    if flag != 0x07:
        raise ValueError("Incorrect packet flag for pitch")
    if not check_version(version):
        raise ValueError("Unsupported protocol version")
    if not verify_checksum(packet):
        raise ValueError("Checksum mismatch")

    explanation = packet[9:9+length].decode('utf-8')

    return {
        "flag": flag,
        "version": version,
        "tone": tone,
        "pitch": pitch,
        "slide_ms": slide_ms,
        "explanation": explanation,
        "valid": True
    }
