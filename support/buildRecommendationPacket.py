"""
buildRecommendationPacket.py

Constructs a Recommendation Packet for the PSSP protocol.

Drafted and created by Bob Greenwade, ChatGPT-4o, and Copilot.
"""

from support.packet_utils import add_header
from support.constants import FLAG_RECOMMEND
import struct

def build_recommendation_packet(start_id: int, end_id: int, rec_type: int, data_value: int) -> bytes:
    """
    Build a Recommendation Packet to suggest phoneme or timing adjustments.

    Parameters:
        start_id (int): ID of first affected phoneme
        end_id (int): ID of last affected phoneme
        rec_type (int): Type of recommendation (01–06)
        data_value (int): Adjustment value (e.g., volume, pitch, timing)

    Returns:
        bytes: Fully constructed packet
    """

    payload = bytearray()
    payload.extend(struct.pack('<H', start_id))     # Start ID (2 bytes)
    payload.extend(struct.pack('<H', end_id))       # End ID (2 bytes)
    payload.append(rec_type)                        # Type (1 byte)
    payload.append(data_value)                      # Data (1 byte)

    return add_header(FLAG_RECOMMEND, payload)
