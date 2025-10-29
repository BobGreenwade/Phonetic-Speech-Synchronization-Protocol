"""
buildVolumePacket.py

Constructs a Volume Packet for the PSSP protocol.

Drafted and created by Bob Greenwade, ChatGPT-4o, and Copilot.
"""

from support.packet_utils import add_header
from support.constants import FLAG_VOLUME
import struct

def build_volume_packet(level: int, explanation: str = "") -> bytes:
    """
    Build a Volume Packet with the given parameters.

    Parameters:
        level (int): Volume level from 0x00 (silent) to 0xFF (maximum shout)
        explanation (str): Optional plain-text explanation of volume change

    Returns:
        bytes: Fully constructed packet
    """

    # Encode explanation string (UTF-8 for plain text)
    explanation_bytes = explanation.encode('utf-8')
    length = len(explanation_bytes)

    # Build payload
    payload = bytearray()
    payload.append(level)                              # Level (1 byte)
    payload.append(length)                             # Length (1 byte)
    payload.extend(explanation_bytes)                  # String (n bytes)

    # Wrap with header and checksum
    return add_header(FLAG_VOLUME, payload)
