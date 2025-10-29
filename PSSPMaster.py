"""
PSSPMaster.py

Master-side orchestrator for PSSP protocol transmission.

Drafted and created by Bob Greenwade, ChatGPT-4o, and Copilot.
"""

from support.building import (
    buildSentencePacket,
    buildPhonemePacket,
    buildVolumePacket,
    buildPitchPacket,
    buildResponsePacket,
    buildRecommendationPacket,
    buildImpedimentPacket,
    buildAcknowledgmentPacket
)

def transmit_sentence(packets: list[bytes]) -> list[bytes]:
    """
    Wraps a full sentence for transmission.

    Parameters:
        packets (list[bytes]): All expressive packets to send

    Returns:
        list[bytes]: Sentence Packet + expressive packets
    """
    sentence_packet = buildSentencePacket.build_sentence_packet(len(packets))
    return [sentence_packet] + packets
