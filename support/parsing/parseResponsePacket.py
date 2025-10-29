"""
parseResponsePacket.py

Parses a Response Packet from the PSSP protocol.

Drafted and created by Bob Greenwade, ChatGPT-4o, and Copilot.
"""

from support.packet_utils import verify_checksum
from support.versioning import check_version

def parse_response_packet(packet: bytes) -> dict:
    """
    Parse a Response Packet.

    Parameters:
        packet (bytes): Raw packet bytes

    Returns:
        dict: Parsed fields including ID, response type, and optional corrective phoneme

    Raises:
        ValueError: If packet is invalid or checksum fails
    """

    if len(packet) < 6:
        raise ValueError("Packet too short for response")

    flag = packet[0]
    version = packet[1]
    id_number = int.from_bytes(packet[2:4], 'little')
    response_type = int.from_bytes(packet[4:6], 'little')

    if flag != 0x02:
        raise ValueError("Incorrect packet flag for response")
    if not check_version(version):
        raise ValueError("Unsupported protocol version")

    # Simple response: Accepted or Abort
    if response_type in [0x0000, 0xFFFF]:
        if len(packet) != 7:
            raise ValueError("Packet length mismatch for simple response")
        if not verify_checksum(packet):
            raise ValueError("Checksum mismatch")
        return {
            "flag": flag,
            "version": version,
            "id": id_number,
            "response_type": response_type,
            "valid": True
        }

    # Complex response: includes corrective phoneme
    if len
