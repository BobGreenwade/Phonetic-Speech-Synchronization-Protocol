# 🔫 PSSP Documentation.md  
**Phonetic Speech Synchronization Protocol — Version 1.0**  
_This is the official canon of the protocol. Yes, we went there._

---

## 📦 Overview

PSSP (Phonetic Speech Synchronization Protocol) is a low-level communication protocol designed to synchronize phonetic speech data with physical or virtual articulators in real time. It supports both audio-to-mechanical and mechanical-to-audio synchronization, enabling expressive, adaptive, and cross-platform speech coordination.

PSSP is modular, packet-based, and versioned. It assumes a Master-Slave architecture, with mutual learning and adaptive feedback. Emotional modulation, environmental awareness, and semantic interpretation are handled by higher-level systems.

---

## 🔁 Architecture

- **Master**: Generates and transmits phonetic, volume, pitch, and timing packets.
- **Slave**: Receives, interprets, and responds with acknowledgment, correction, or recommendation packets.
- **Bidirectional**: Supports both audio-to-mechanical and mechanical-to-audio flows.

---

## 📜 Packet Structure

All packets begin with:

- `Flag` (1 byte): Packet type identifier  
- `Version` (1 byte): Protocol version (default: `01`)  
- Followed by packet-specific fields  
- `Checksum` (1 byte): XOR of all preceding bytes

---

## 🎙️ Master Packets

### Sentence Packet `[Flag: 01]`
- `Count` (2 bytes): Number of packets in the sentence  
- `Checksum` (1 byte)

### Phoneme Packet `[Flag: 03]`
- `ID Number` (2 bytes)  
- `Type` (1 byte): 0–Silent, 1–Subdued, 2–Normal, 3–Exaggerated  
- `Offset` (4 bytes): Delay in ms  
- `Duration` (4 bytes): Expected duration  
- `Length` (1 byte): UTF-16 character count  
- `Data` (n bytes): IPA phoneme string  
- `Checksum` (1 byte)

### Volume Packet `[Flag: 05]`
- `Level` (1 byte): 00–FF scale  
- `Length` (1 byte): Length of explanation string  
- `String` (n bytes): Optional explanation  
- `Checksum` (1 byte)

### Pitch Packet `[Flag: 07]`
- `Tone` (1 byte)  
- `Pitch` (1 byte)  
- `Slide` (4 bytes): Pitch slide duration  
- `Length` (1 byte): Length of explanation string  
- `String` (n bytes): Optional explanation  
- `Checksum` (1 byte)

---

## 🤖 Slave Packets

### Abort Packet `[Flag: 00]`
- Four bytes of `[00]`  
- Cancels all ongoing activity

### Response Packet `[Flag: 02]`
- `ID Number` (2 bytes): Matches phoneme  
- `Type` (2 bytes): 0000–Accepted, FFFF–Abort, Bitfield for adjustments  
- Optional:  
  - `Duration` (4 bytes)  
  - `Length` (1 byte)  
  - `Data` (n bytes): Corrective phoneme  
- `Checksum` (1 byte)

### Acknowledgment Packet `[Flag: 04]`
- `Length` (2 bytes): Final sentence length  
- `Code` (2 bytes): Always `[1B][1B]`  
- `Checksum` (1 byte)

### Recommendation Packet `[Flag: 06]`
- `Start ID` (2 bytes)  
- `End ID` (2 bytes)  
- `Type` (1 byte): 01–06  
- `Data` (1 byte): Adjustment value  
- `Checksum` (1 byte)

### Impediment Packet `[Flag: 08]`
- `Type` (1 byte): 01–Muffled, 02–Restrictive, 03–Chewing, 04–Face restriction, FF–Damage  
- `Severity` (1 byte): 00–FF  
- `Length` (1 byte): Length of explanation string  
- `String` (n bytes): Optional explanation

---

## 🧠 Design Principles

- **Versioned**: All packets include a version byte for compatibility
- **Extensible**: Hooks included for emotional, environmental, and semantic layers
- **Adaptable**: Slave can recommend corrections or simulate impediments
- **Cross-platform**: Suitable for SPI, serial, wireless, or abstract buses

---

## 🛠 Future Enhancements (Hooks Present)

- Emotional expressiveness  
- Timing calibration  
- Security/authentication  
- Environmental awareness  
- Registry integration for source validation

---

## 🧭 Use Cases

- VTubing and avatar animation  
- Animatronic speech coordination  
- Assistive speech devices  
- AI-driven character embodiment  
- Robotic or hybrid speech systems
