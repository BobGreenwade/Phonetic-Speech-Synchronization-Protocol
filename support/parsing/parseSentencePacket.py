"""
parseSentencePacket.py

Parses a Sentence Packet from the PSSP protocol.

Drafted and created by Bob Greenwade, ChatGPT-4o, and Copilot.
"""

from support.packet_utils import verify_checksum
from support.versioning import check_version

def parse_sentence_packet(packet: bytes) -> dict:
    """
    Parse a Sentence Packet.

    Parameters:
        packet (bytes): Raw packet bytes

    Returns:
        dict: Parsed fields including packet count

    Raises:
        ValueError: If packet is invalid or checksum fails
    """

    if len(packet) != 5:
        raise ValueError("Incorrect packet length for sentence")

    flag = packet[0]
    version = packet[1]
    packet_count = int.from_bytes(packet[2:4], 'little')

    if flag != 0x01:
        raise ValueError("Incorrect packet flag for sentence")
    if not check_version(version):
        raise ValueError("Unsupported protocol version")
    if not verify_checksum(packet):
        raise ValueError("Checksum mismatch")

    return {
        "flag": flag,
        "version": version,
        "packet_count": packet_count,
        "valid": True
    }
