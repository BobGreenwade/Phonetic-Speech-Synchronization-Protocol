"""
buildResponsePacket.py

Constructs a Response Packet for the PSSP protocol.

Drafted and created by Bob Greenwade, ChatGPT-4o, and Copilot.
"""

from support.packet_utils import add_header
from support.constants import FLAG_RESPONSE
import struct

def build_response_packet(
    id_number: int,
    response_type: int,
    corrective_phoneme: str = "",
    duration_ms: int = 0,
    adjustments: list[int] = []
) -> bytes:
    """
    Build a Response Packet for a received phoneme.

    Parameters:
        id_number (int): ID of the original phoneme packet
        response_type (int): 0x0000 (Accepted), 0xFFFF (Abort), or bitfield
        corrective_phoneme (str): Optional UTF-16 phoneme string
        duration_ms (int): Duration of corrective phoneme
        adjustments (list[int]): Optional adjustment values (volume, pitch, breathing)

    Returns:
        bytes: Fully constructed packet
    """

    payload = bytearray()
    payload.extend(struct.pack('<H', id_number))         # ID Number (2 bytes)
    payload.extend(struct.pack('<H', response_type))     # Type (2 bytes)

    if response_type not in [0x0000, 0xFFFF]:
        phoneme_bytes = corrective_phoneme.encode('utf-16le')
        length = len(phoneme_bytes)
        payload.extend(struct.pack('<I', duration_ms))   # Duration (4 bytes)
        payload.append(length)                           # Length (1 byte)
        payload.extend(phoneme_bytes)                    # Data (n bytes)
        for adj in adjustments:
            payload.append(adj)                          # Adjustment values (1 byte each)

    return add_header(FLAG_RESPONSE, payload)
