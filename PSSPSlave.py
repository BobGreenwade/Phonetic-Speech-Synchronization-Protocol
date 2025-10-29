"""
PSSPSlave.py

Slave-side orchestrator for PSSP protocol reception and parsing.

Drafted and created by Bob Greenwade, ChatGPT-4o, and Copilot.
"""

from support.parsing import (
    parseSentencePacket,
    parsePhonemePacket,
    parseVolumePacket,
    parsePitchPacket,
    parseResponsePacket,
    parseRecommendationPacket,
    parseImpedimentPacket,
    parseAcknowledgmentPacket
)

def interpret_packet(packet: bytes) -> dict:
    """
    Dispatches packet to appropriate parser.

    Parameters:
        packet (bytes): Raw packet bytes

    Returns:
        dict: Parsed packet contents
    """

    flag = packet[0]

    dispatch = {
        0x01: parseSentencePacket.parse_sentence_packet,
        0x02: parseResponsePacket.parse_response_packet,
        0x03: parsePhonemePacket.parse_phoneme_packet,
        0x04: parseAcknowledgmentPacket.parse_acknowledgment_packet,
        0x05: parseVolumePacket.parse_volume_packet,
        0x06: parseRecommendationPacket.parse_recommendation_packet,
        0x07: parsePitchPacket.parse_pitch_packet,
        0x08: parseImpedimentPacket.parse_impediment_packet
    }

    if flag not in dispatch:
        raise ValueError(f"Unknown packet flag: {hex(flag)}")

    return dispatch[flag](packet)
