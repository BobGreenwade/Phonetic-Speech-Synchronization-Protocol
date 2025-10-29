"""
buildSentencePacket.py

Constructs a Sentence Packet for the PSSP protocol.

Drafted and created by Bob Greenwade, ChatGPT-4o, and Copilot.
"""

from support.packet_utils import add_header
from support.constants import FLAG_SENTENCE
import struct

def build_sentence_packet(packet_count: int) -> bytes:
    """
    Build a Sentence Packet to declare the number of packets in the sentence.

    Parameters:
        packet_count (int): Total number of packets in the sentence (excluding this one)

    Returns:
        bytes: Fully constructed packet
    """

    # Build payload: Count (2 bytes)
    payload = struct.pack('<H', packet_count)

    # Wrap with header and checksum
    return add_header(FLAG_SENTENCE, payload)
