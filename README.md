# OLFYN — Open Scent Protocol (OSP)

> *"The open standard for digital scent transmission."*

[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)
[![Version](https://img.shields.io/badge/OSP-v1.1-blue.svg)](SPECIFICATION.md)
[![Status](https://img.shields.io/badge/Status-Draft-orange.svg)](SPECIFICATION.md)
[![Validate examples](https://github.com/olfyn/olfyn-osp-spec/actions/workflows/validate.yml/badge.svg)](.github/workflows/validate.yml)

**Contributors wanted.** OSP is an early draft and we are looking for people to help shape it: hardware makers, firmware and backend developers, chemists, perfumers, sommeliers, and researchers. See [How to contribute](#how-to-contribute).

---

## What is OSP?

Vision was digitized with photography. Sound was digitized with audio. Touch was digitized with haptics. **Scent has not been digitized yet.**

The **Open Scent Protocol (OSP)** is an open standard for representing, transmitting, and reproducing scent. It does for smell what RGB does for color: any scent is described as a mix of **10 aromatic dimensions**, each from `0.0` (absent) to `1.0` (maximum), and travels between devices as JSON over REST or WebSocket.

```json
{
  "floral": 0.0, "frutal": 0.0, "herbal": 0.0, "leñoso": 0.0, "ahumado": 0.0,
  "especiado": 0.0, "animal": 0.0, "químico": 0.0, "marino": 0.0, "dulce": 0.0
}
```

The dimension keys are in Spanish (floral, fruity, herbal, woody, smoky, spicy, animal, chemical, marine, sweet) and are part of the wire format.

## Why: the most human use cases first

| Profile | Use case | Creation method |
|---|---|---|
| 🧠 **Memory** | Personally meaningful scents for memory and reminiscence activities, e.g. with people living with dementia | Hybrid capture |
| 💑 **Presence** | Sharing a loved one's scent across distance | Hybrid capture |
| 🕊️ **Remembrance** | Preserving the scent of someone who has passed | Hybrid capture |
| 🍷 **Sommelier** | Wine aromas at a distance | Predefined (documented chemistry) |
| 💐 **Perfumery** | Trying a perfume before buying it online | Predefined (published notes) |

> **Not a medical device.** OSP is a data format. It makes no therapeutic or clinical claims. Any health-related use must follow the guidance of qualified professionals and the regulations that apply where it is used.

## Hybrid capture (new in v1.1)

How a personal scent signature is created:

```
STEP 1 — A BME688 sensor reads the object (clothing, flowers, any scented item)
         → VOC index, volatility, temperature, humidity
STEP 2 — The person describes it in their own words
         "Sweet, floral, a hint of wood..."
STEP 3 — An AI model combines both sources
         → a 10-dimension OSP profile with a confidence score
STEP 4 — The person fine-tunes it with sliders and saves it
```

## Quick example — a personal scent signature

```json
{
  "osp_version": "1.1",
  "scent_id": "memoria_jardin_mama_001",
  "name": "El jardín de mamá",
  "created_at": "2026-07-01T10:30:00Z",
  "profile": {
    "floral":    0.45,
    "herbal":    0.25,
    "dulce":     0.15,
    "leñoso":    0.10,
    "marino":    0.05,
    "frutal":    0.00,
    "ahumado":   0.00,
    "especiado": 0.00,
    "animal":    0.00,
    "químico":   0.00
  },
  "intensity":   0.65,
  "duration_ms": 300000,
  "fade_in_ms":  3000,
  "fade_out_ms": 8000,
  "capture": {
    "method": "hybrid",
    "sensor_data": {
      "voc_index":     312,
      "dominant_note": "floral",
      "volatility":    "medium"
    },
    "verbal_description": "El jardín de mamá. Lavanda, algo de tierra húmeda y una flor que no sé cómo se llama.",
    "ai_model":   "claude-haiku-4-5",
    "confidence": 0.74
  },
  "metadata": {
    "category": "memoria",
    "person":   "Mamá",
    "tags":     ["memoria", "jardín", "familia"]
  }
}
```

## Validate a profile

A small reference validator checks profiles against the JSON Schema:

```bash
pip install "jsonschema[format]"
python tools/validate.py my-profile.json
python tools/validate.py examples/EXAMPLES.md   # validates every profile in a Markdown file
```

CI runs it on the examples and this README on every push and pull request.

## Documentation

| Document | Description |
|---|---|
| [SPECIFICATION.md](SPECIFICATION.md) | Full OSP v1.1 technical specification |
| [schema/osp-profile-v1.1.json](schema/osp-profile-v1.1.json) | JSON Schema for profiles |
| [examples/EXAMPLES.md](examples/EXAMPLES.md) | Sample profiles for all 5 categories, plus a session |
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [versions/v1.0/](versions/v1.0/) | Previous version (v1.0) |

## Reference hardware

| Component | Role | Approx. price |
|---|---|---|
| Raspberry Pi Zero 2W | OSP server + Wi-Fi | ~$15 |
| BME688 | VOC sensor for hybrid capture | ~$12 |
| Ultrasonic mist maker | Aroma diffusion | ~$10 |
| Arduino Nano | Pump control | ~$5 |
| HC-05 Bluetooth | Local wireless | ~$4 |
| Accessories | Breadboard, cables, SD card, PSU | ~$22 |
| Base scent cartridges (6) | Floral, sweet, wood, musk, fruit, herbal | ~$12 |

**Estimated prototype cost: ~$80 USD.** This is a reference bill of materials; no reference build is published yet.

## Project status

| Area | Status |
|---|---|
| Specification | v1.1 draft (v1.0: June 2026, v1.1: July 2026) |
| JSON Schema | v1.1 |
| Reference validator | Available (`tools/validate.py`) |
| Reference server / firmware | Not started — help wanted |
| Hardware prototype | Bill of materials defined; no published build yet |

## Roadmap

| Version | Target | Features |
|---|---|---|
| OSP 1.0 | Released 2026-06 | Base specification |
| OSP 1.1 | Released 2026-07 | Hybrid capture, BME688, 5 categories |
| OSP 1.2 | Q1 2027 | Adaptive sessions |
| OSP 2.0 | 2028 | Encrypted personal signatures |

## How to contribute

Good places to start:

- **Review the spec** and open an issue for anything unclear, inconsistent or missing.
- **Build a reference server** (REST + WebSocket) or device firmware.
- **Build the reference hardware** and share photos, notes and measurements.
- **Contribute predefined profiles** (wines, perfumes) with their sources.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Everyone taking part follows our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

MIT — see [LICENSE](LICENSE).

---

*Created by Franklin Rodriguez · Panama City, Panama*
