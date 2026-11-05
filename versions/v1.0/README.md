# OLFYN — Open Scent Protocol (OSP)

> *"The open standard for digital scent transmission"*

[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)
[![Version](https://img.shields.io/badge/OSP-v1.0-blue.svg)](SPECIFICATION.md)
[![Status](https://img.shields.io/badge/Status-Draft-orange.svg)](SPECIFICATION.md)

---

## What is OSP?

The **Open Scent Protocol (OSP)** is an open standard for representing, transmitting, and reproducing digital olfactory experiences.

OSP does for scent what RGB does for color — it describes any smell as a combination of 10 primary aromatic dimensions, transmissible between any compatible device via JSON over REST or WebSocket.

---

## Why?

Vision was digitized with photography.  
Sound was digitized with audio.  
Touch was digitized with haptics.  
**Scent has not been digitized yet.**

OSP is the foundation to change that — starting with the most human use cases:

| Use Case | Description |
|---|---|
| 🧠 **Memory** | Olfactory therapy for Alzheimer's patients |
| 💑 **Presence** | Sharing personal scent signatures between loved ones at distance |
| 🕊️ **Remembrance** | Preserving and accessing the scent of someone who has passed |

---

## The 10 Aromatic Dimensions

Any smell can be described as a combination of these 10 primary dimensions:

```json
{
  "floral":    0.0,
  "frutal":    0.0,
  "herbal":    0.0,
  "leñoso":    0.0,
  "ahumado":   0.0,
  "especiado": 0.0,
  "animal":    0.0,
  "químico":   0.0,
  "marino":    0.0,
  "dulce":     0.0
}
```

Each value ranges from `0.0` (absent) to `1.0` (maximum intensity).

---

## Quick Example

```json
{
  "osp_version": "1.0",
  "scent_id": "olfyn_lavanda_001",
  "name": "Lavender from mom's garden",
  "profile": {
    "floral":    0.65,
    "herbal":    0.25,
    "leñoso":    0.05,
    "dulce":     0.05,
    "frutal":    0.00,
    "ahumado":   0.00,
    "especiado": 0.00,
    "animal":    0.00,
    "marino":    0.00,
    "químico":   0.00
  },
  "intensity":   0.70,
  "duration_ms": 300000,
  "fade_in_ms":  2000,
  "fade_out_ms": 5000,
  "metadata": {
    "category": "memoria",
    "tags": ["alzheimer", "memory", "garden"]
  }
}
```

---

## Documentation

| Document | Description |
|---|---|
| [SPECIFICATION.md](SPECIFICATION.md) | Full OSP v1.0 technical specification |
| [SCHEMA.json](schema/osp-profile-v1.0.json) | JSON Schema for validation |
| [EXAMPLES.md](examples/EXAMPLES.md) | Sample OSP profiles |
| [CHANGELOG.md](CHANGELOG.md) | Version history |

---

## OSP Ecosystem

```
OLFYN App (iOS / Android)
        │
        ▼
OLFYN Cloud (API)
        │
        ▼
OLFYN One (Hardware Device)
        │
        ├── 6 scent cartridges
        ├── Ultrasonic diffuser
        └── OSP-compatible firmware
```

---

## Roadmap

| Version | ETA | Features |
|---|---|---|
| OSP 1.0 | Q3 2026 | Base spec — profiles, REST API, WebSocket, OLFYN DB |
| OSP 1.1 | Q1 2027 | Scent capture support (sensor → profile) |
| OSP 1.2 | Q2 2027 | Adaptive sessions (user response modifies sequence) |
| OSP 2.0 | 2028 | Personal scent signatures, encrypted private profiles |

---

## Contributing

OSP is open. We welcome:
- New OSP profile examples
- Implementations in any language
- Hardware integrations
- Clinical research collaborations

Open an [Issue](../../issues) or submit a [Pull Request](../../pulls).

---

## License

MIT License — see [LICENSE](LICENSE)

---

*OLFYN · olfyn.io · June 2026*
