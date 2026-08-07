# OLFYN — Open Scent Protocol (OSP)

> *"The open standard for digital scent transmission"*

[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)
[![Version](https://img.shields.io/badge/OSP-v1.1-blue.svg)](SPECIFICATION.md)
[![Status](https://img.shields.io/badge/Status-Draft-orange.svg)](SPECIFICATION.md)

---

## What is OSP?

The **Open Scent Protocol (OSP)** is an open standard for representing, transmitting, and reproducing digital olfactory experiences.

OSP does for scent what RGB does for color — any smell can be described as a combination of 10 primary aromatic dimensions, transmissible between devices via JSON over REST or WebSocket.

---

## Why?

Vision was digitized with photography.  
Sound was digitized with audio.  
Touch was digitized with haptics.  
**Scent has not been digitized yet.**

OSP is the foundation to change that — starting with the most human use cases:

| Profile | Use Case | Creation Method |
|---|---|---|
| 🧠 **Memory** | Olfactory therapy for Alzheimer's | Hybrid capture (BME688 + AI) |
| 💑 **Presence** | Sharing personal scent at distance | Hybrid capture (BME688 + AI) |
| 🕊️ **Remembrance** | Preserving the scent of someone lost | Hybrid capture (BME688 + AI) |
| 🍷 **Sommelier** | Wine aromas at distance | Predefined (documented chemistry) |
| 💐 **Perfumery** | Try perfumes before buying online | Predefined (published notes) |

---

## What's new in v1.1

- **Hybrid Capture** — New method combining BME688 sensor readings + verbal description + AI synthesis to create personal scent signatures
- **New endpoint** `POST /v1/capture` — hybrid capture pipeline
- **BME688 replaces MQ sensors** — purpose-built VOC sensor vs industrial gas detectors
- **5 profile categories** — added `vinos` and `perfumeria`
- **`capture` field in OSP object** — documents how each profile was created

---

## The 10 Aromatic Dimensions

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

Each value: `0.0` (absent) → `1.0` (maximum intensity)

---

## Hybrid Capture — How it works

```
STEP 1 — BME688 sensor reads the object
         (clothing, flowers, any scented item)
         → VOC index, volatility, temperature, humidity

STEP 2 — User describes in words
         "Sweet, floral, a hint of wood..."

STEP 3 — AI synthesizes both sources
         → Generates OSP profile of 10 dimensions

STEP 4 — User fine-tunes sliders
         → Profile saved to OLFYN DB
```

---

## Quick Example — Personal Scent Signature

```json
{
  "osp_version": "1.1",
  "scent_id": "memoria_jardin_mama_001",
  "name": "El jardín de mamá",
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
    "method":              "hybrid",
    "sensor_data": {
      "voc_index":         312,
      "dominant_note":     "floral",
      "volatility":        "medium"
    },
    "verbal_description":  "El jardín de mamá. Lavanda, algo de tierra húmeda y una flor que no sé cómo se llama.",
    "ai_model":            "claude-haiku-4-5",
    "confidence":          0.74
  },
  "metadata": {
    "category": "memoria",
    "person":   "Mamá",
    "tags":     ["alzheimer", "memoria", "jardín", "terapia"]
  }
}
```

---

## Documentation

| Document | Description |
|---|---|
| [SPECIFICATION.md](SPECIFICATION.md) | Full OSP v1.1 technical specification |
| [SCHEMA.json](schema/osp-profile-v1.1.json) | JSON Schema for validation |
| [EXAMPLES.md](examples/EXAMPLES.md) | Sample OSP profiles — all 5 categories |
| [CHANGELOG.md](CHANGELOG.md) | Version history |

---

## Hardware Reference

| Component | Role | Price |
|---|---|---|
| Raspberry Pi Zero 2W | OSP server + WiFi | ~$15 |
| **BME688** (replaces MQ kit) | VOC sensor for hybrid capture | ~$12 |
| Ultrasonic mist maker | Aroma diffusion | ~$10 |
| Arduino Nano | Pump control | ~$5 |
| HC-05 Bluetooth | Local wireless | ~$4 |
| Accessories | Breadboard, cables, SD, PSU | ~$22 |
| Base scent cartridges (6) | Floral, sweet, wood, musk, fruit, herbal | ~$12 |

**Total prototype: ~$80 USD**

---

## Roadmap

| Version | ETA | Features |
|---|---|---|
| OSP 1.0 | 2026-06-01 | Base spec |
| OSP 1.1 | 2026-07-01 | Hybrid capture, BME688, 5 categories |
| OSP 1.2 | Q1 2027 | Adaptive sessions |
| OSP 2.0 | 2028 | Encrypted personal signatures |

---

## License

MIT License — see [LICENSE](LICENSE)

---

*OLFYN · olfyn.io · July 2026*
