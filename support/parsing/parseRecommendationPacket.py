"""
parseRecommendationPacket.py

Parses a Recommendation Packet from the PSSP protocol.

Drafted and created by Bob Greenwade, ChatGPT-4o, and Copilot.
"""

from support.packet_utils import verify_checksum
from support.versioning import check_version

def parse_recommendation_packet(packet: bytes) -> dict:
    """
    Parse a Recommendation Packet.

    Parameters:
        packet (bytes): Raw packet bytes

    Returns:
        dict: Parsed fields including phoneme range, recommendation type, and value

    Raises:
        ValueError: If packet is invalid or checksum fails
    """

    if len(packet) != 8:
        raise ValueError("Incorrect packet length for recommendation")

    flag = packet[0]
    version = packet[1]
    start_id = int.from_bytes(packet[2:4], 'little')
    end_id = int.from_bytes(packet[4:6], 'little')
    rec_type = packet[6]
    data_value = packet[7]

    if flag != 0x06:
        raise ValueError("Incorrect packet flag for recommendation")
    if not check_version(version):
        raise ValueError("Unsupported protocol version")
    if not verify_checksum(packet):
        raise ValueError("Checksum mismatch")

    return {
        "flag": flag,
        "version": version,
        "start_id": start_id,
        "end_id": end_id,
        "recommendation_type": rec_type,
        "value": data_value,
        "valid": True
    }
