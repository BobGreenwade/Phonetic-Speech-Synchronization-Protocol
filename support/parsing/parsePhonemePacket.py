"""
parsePhonemePacket.py

Parses a Phoneme Packet from the PSSP protocol.

Drafted and created by Bob Greenwade, ChatGPT-4o, and Copilot.
"""

from support.packet_utils import verify_checksum
from support.versioning import check_version

def parse_phoneme_packet(packet: bytes) -> dict:
    """
    Parse a Phoneme Packet.

    Parameters:
        packet (bytes): Raw packet bytes

    Returns:
        dict: Parsed fields including ID, type, timing, and phoneme string

    Raises:
        ValueError: If packet is invalid or checksum fails
    """

    if len(packet) < 13:
        raise ValueError("Packet too short for phoneme")

    flag = packet[0]
    version = packet[1]
    id_number = int.from_bytes(packet[2:4], 'little')
    phoneme_type = packet[4]
    offset_ms = int.from_bytes(packet[5:9], 'little')
    duration_ms = int.from_bytes(packet[9:13], 'little')
    length = packet[13]

    expected_len = 14 + length + 1
    if len(packet) != expected_len:
        raise ValueError("Packet length mismatch")
    if flag != 0x03:
        raise ValueError("Incorrect packet flag for phoneme")
    if not check_version(version):
        raise ValueError("Unsupported protocol version")
    if not verify_checksum(packet):
        raise ValueError("Checksum mismatch")

    phoneme_bytes = packet[14:-1]
    phoneme_string = phoneme_bytes.decode('utf-16le')

    return {
        "flag": flag,
        "version": version,
        "id": id_number,
        "type": phoneme_type,
        "offset_ms": offset_ms,
        "duration_ms": duration_ms,
        "phoneme": phoneme_string,
        "valid": True
    }
