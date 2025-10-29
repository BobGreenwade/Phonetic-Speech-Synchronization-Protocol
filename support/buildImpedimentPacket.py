"""
buildImpedimentPacket.py

Constructs an Impediment Packet for the PSSP protocol.

Drafted and created by Bob Greenwade, ChatGPT-4o, and Copilot.
"""

from support.packet_utils import add_header
from support.constants import FLAG_IMPEDIMENT
import struct

def build_impediment_packet(imp_type: int, severity: int, explanation: str = "") -> bytes:
    """
    Build an Impediment Packet to simulate physical speech constraints.

    Parameters:
        imp_type (int): Type of impediment (01–04, FF)
        severity (int): Severity from 0x00 (none) to 0xFF (complete stoppage)
        explanation (str): Optional string for finer detail

    Returns:
        bytes: Fully constructed packet
    """

    explanation_bytes = explanation.encode('utf-8')
    length = len(explanation_bytes)

    payload = bytearray()
    payload.append(imp_type)                         # Type (1 byte)
    payload.append(severity)                         # Severity (1 byte)
    payload.append(length)                           # Length (1 byte)
    payload.extend(explanation_bytes)                # String (n bytes)

    return add_header(FLAG_IMPEDIMENT, payload)
