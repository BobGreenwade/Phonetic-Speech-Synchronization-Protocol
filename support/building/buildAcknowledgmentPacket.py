"""
buildAcknowledgmentPacket.py

Constructs an Acknowledgment Packet for the PSSP protocol.

Drafted and created by Bob Greenwade, ChatGPT-4o, and Copilot.
"""

from support.packet_utils import add_header
from support.constants import FLAG_ACKNOWLEDGE
import struct

def build_acknowledgment_packet(sentence_length: int) -> bytes:
    """
    Build an Acknowledgment Packet to confirm sentence receipt.

    Parameters:
        sentence_length (int): Final packet count in the sentence

    Returns:
        bytes: Fully constructed packet
    """

    payload = bytearray()
    payload.extend(struct.pack('<H', sentence_length))  # Length (2 bytes)
    payload.extend(b'\x1B\x1B')                          # Code (2 bytes)

    return add_header(FLAG_ACKNOWLEDGE, payload)
