"""
parseImpedimentPacket.py

Parses an Impediment Packet from the PSSP protocol.

Drafted and created by Bob Greenwade, ChatGPT-4o, and Copilot.
"""

from support.packet_utils import verify_checksum
from support.versioning import check_version

def parse_impediment_packet(packet: bytes) -> dict:
    """
    Parse an Impediment Packet.

    Parameters:
        packet (bytes): Raw packet bytes

    Returns:
        dict: Parsed fields including type, severity, and explanation

    Raises:
        ValueError: If packet is invalid or checksum fails
    """

    if len(packet) < 5:
        raise ValueError("Packet too short for impediment")

    flag = packet[0]
    version = packet[1]
    imp_type = packet[2]
    severity = packet[3]
    length = packet[4]

    if flag != 0x08:
        raise ValueError("Incorrect packet flag for impediment")
    if not check_version(version):
        raise ValueError("Unsupported protocol version")
    if len(packet) != 5 + length + 1:
        raise ValueError("Packet length mismatch")
    if not verify_checksum(packet):
        raise ValueError("Checksum mismatch")

    explanation = packet[5:5+length].decode('utf-8')

    return {
        "flag": flag,
        "version": version,
        "type": imp_type,
        "severity": severity,
        "explanation": explanation,
        "valid": True
    }
