"""
buildPitchPacket.py

Constructs a Pitch Packet for the PSSP protocol.

Drafted and created by Bob Greenwade, ChatGPT-4o, and Copilot.
"""

from support.packet_utils import add_header
from support.constants import FLAG_PITCH
import struct

def build_pitch_packet(tone: int, pitch: int, slide_ms: int, explanation: str = "") -> bytes:
    """
    Build a Pitch Packet with the given parameters.

    Parameters:
        tone (int): Tone identifier (e.g., emotional, musical, character voice)
        pitch (int): Pitch level (0x00 to 0xFF)
        slide_ms (int): Duration of pitch slide in milliseconds
        explanation (str): Optional plain-text explanation of pitch change

    Returns:
        bytes: Fully constructed packet
    """

    explanation_bytes = explanation.encode('utf-8')
    length = len(explanation_bytes)

    # Build payload
    payload = bytearray()
    payload.append(tone)                                # Tone (1 byte)
    payload.append(pitch)                               # Pitch (1 byte)
    payload.extend(struct.pack('<I', slide_ms))         # Slide (4 bytes)
    payload.append(length)                              # Length (1 byte)
    payload.extend(explanation_bytes)                   # String (n bytes)

    # Wrap with header and checksum
    return add_header(FLAG_PITCH, payload)
