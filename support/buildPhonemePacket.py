"""
buildPhonemePacket.py

Constructs a Phoneme Packet for the PSSP protocol.

Drafted and created by Bob Greenwade, ChatGPT-4o, and Copilot.
"""

from support.packet_utils import add_header
from support.constants import FLAG_PHONEME
import struct

def build_phoneme_packet(
    id_number: int,
    phoneme_type: int,
    offset_ms: int,
    duration_ms: int,
    phoneme_string: str
) -> bytes:
    """
    Build a Phoneme Packet with the given parameters.

    Parameters:
        id_number (int): Sequence number within the sentence
        phoneme_type (int): 0–Silent, 1–Subdued, 2–Normal, 3–Exaggerated
        offset_ms (int): Delay after previous phoneme (ms)
        duration_ms (int): Expected duration of this phoneme (ms)
        phoneme_string (str): IPA phoneme string (UTF-16)

    Returns:
        bytes: Fully constructed packet
    """

    # Encode phoneme string as UTF-16LE (without BOM)
    phoneme_bytes = phoneme_string.encode('utf-16le')
    length = len(phoneme_bytes)

    # Build payload
    payload = bytearray()
    payload.extend(struct.pack('<H', id_number))       # ID Number (2 bytes)
    payload.append(phoneme_type)                        # Type (1 byte)
    payload.extend(struct.pack('<I', offset_ms))        # Offset (4 bytes)
    payload.extend(struct.pack('<I', duration_ms))      # Duration (4 bytes)
    payload.append(length)                              # Length (1 byte)
    payload.extend(phoneme_bytes)                       # Data (n bytes)

    # Wrap with header and checksum
    return add_header(FLAG_PHONEME, payload)
