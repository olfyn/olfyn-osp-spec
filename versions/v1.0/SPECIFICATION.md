# OSP v1.0 — Open Scent Protocol Technical Specification

**Version:** 1.0  
**Status:** Draft  
**Date:** 2026-06-01  
**License:** MIT  
**Repository:** github.com/olfyn/olfyn-osp-spec  

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Data Model — The OSP Object](#2-data-model)
3. [OSP Sessions](#3-osp-sessions)
4. [Transport Protocol](#4-transport-protocol)
5. [Device Capabilities](#5-device-capabilities)
6. [OLFYN DB](#6-olfyn-db)
7. [Error Codes](#7-error-codes)
8. [OSP Compatible Certification](#8-certification)
9. [Versioning](#9-versioning)
10. [Extensions](#10-extensions)
11. [Governance](#11-governance)

---

## 1. Introduction

### 1.1 Purpose

The Open Scent Protocol (OSP) defines a standard way to represent, transmit, and reproduce olfactory experiences digitally. It is hardware-agnostic, extensible, and JSON-based.

### 1.2 Reference Analogies

| Protocol | Domain | Analogy with OSP |
|---|---|---|
| RGB / HEX | Digital color | OSP describes scents as 10 dimensions, like RGB combines 3 primaries |
| MIDI | Digital music | OSP defines "olfactory notes" with intensity and duration |
| HTTP | Web transfer | OSP defines standard endpoints for requesting and delivering scent profiles |
| OSC | Media control | OSP enables real-time control of olfactory actuators |

### 1.3 Terminology

| Term | Definition |
|---|---|
| Scent Profile | Digital representation of a smell as an OSP JSON object |
| Actuator | Physical device that releases scents (e.g. OLFYN One) |
| Emitter | Device or system that sends OSP profiles |
| Receiver | Device or system that receives and executes OSP profiles |
| OLFYN DB | Public database of registered OSP profiles |
| Intensity | Magnitude of scent release, value 0.0 to 1.0 |
| Dimension | One of the 10 primary aromatic categories |
| Session | Ordered sequence of OSP profiles with defined timing |

---

## 2. Data Model

### 2.1 Full OSP Profile Object

```json
{
  "osp_version":  "1.0",
  "scent_id":     "string",
  "name":         "string",
  "description":  "string",
  "author":       "string",
  "created_at":   "ISO 8601",
  "updated_at":   "ISO 8601",

  "profile": {
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
  },

  "intensity":    0.75,
  "duration_ms":  5000,
  "fade_in_ms":   500,
  "fade_out_ms":  1000,
  "repeat":       1,
  "interval_ms":  0,

  "metadata": {
    "category":   "memoria|presencia|recuerdo|wellness|general",
    "person":     "string",
    "tags":       ["string"],
    "notes":      "string",
    "language":   "es|en|..."
  },

  "extensions": {
    "x-vendor-key": "value"
  }
}
```

### 2.2 Required vs Optional Fields

| Field | Required | Notes |
|---|---|---|
| osp_version | ✅ | Must be "1.0" for this spec |
| scent_id | ✅ | Globally unique identifier |
| name | ✅ | Human-readable name |
| profile | ✅ | All 10 dimensions must be present |
| intensity | ✅ | 0.0 to 1.0 |
| duration_ms | ✅ | Duration in milliseconds |
| created_at | ✅ | ISO 8601 timestamp |
| description | ❌ | Optional |
| fade_in_ms | ❌ | Default: 0 |
| fade_out_ms | ❌ | Default: 0 |
| repeat | ❌ | Default: 1 |
| metadata | ❌ | Optional but recommended |
| extensions | ❌ | Vendor-specific fields |

### 2.3 The 10 Aromatic Dimensions

| Dimension | Description | Natural Examples |
|---|---|---|
| floral | Flower aromas | Rose, jasmine, lavender, violet |
| frutal | Fruit aromas | Citrus, mango, strawberry, apple |
| herbal | Green and herbaceous | Cut grass, mint, basil, eucalyptus |
| leñoso | Wood and earth | Cedar, sandalwood, moss, pine |
| ahumado | Combustion aromas | Smoke, charcoal, tobacco |
| especiado | Warm and spicy | Cinnamon, pepper, cardamom |
| animal | Body and animal | Musk, leather, amber, wax |
| químico | Synthetic and industrial | Acrid, medicinal, plastic |
| marino | Aquatic and saline | Sea, seaweed, rain, humid air |
| dulce | Sweet aromas | Vanilla, caramel, honey, coconut |

> **Rule:** The sum of all dimensions does not need to equal 1.0. Each dimension is independent. However, it is recommended that the total sum not exceed 3.0 for credible, reproducible profiles.

---

## 3. OSP Sessions

A session is an ordered sequence of OSP profiles with defined start times. Sessions are the primary mechanism for Alzheimer therapy protocols.

```json
{
  "osp_version":       "1.0",
  "session_id":        "string",
  "session_name":      "string",
  "created_at":        "ISO 8601",
  "category":          "memoria|wellness|therapy|custom",
  "total_duration_ms": 1200000,

  "sequence": [
    {
      "offset_ms":          0,
      "scent_id":           "olfyn_lavanda_001",
      "intensity_override": 0.60,
      "label":              "Calming opening"
    },
    {
      "offset_ms": 300000,
      "scent_id":  "olfyn_vainilla_001",
      "label":     "Home memory"
    },
    {
      "offset_ms": 600000,
      "scent_id":  "personal_mom_garden",
      "label":     "Family garden"
    }
  ],

  "log_responses": true,
  "metadata": {
    "patient":   "string",
    "therapist": "string",
    "notes":     "string"
  }
}
```

---

## 4. Transport Protocol

### 4.1 REST API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /v1/profiles | List all available profiles |
| GET | /v1/profiles/{scent_id} | Get a specific OSP profile |
| POST | /v1/profiles | Upload a new OSP profile |
| DELETE | /v1/profiles/{scent_id} | Delete a profile |
| POST | /v1/emit | Activate a profile immediately |
| POST | /v1/emit/stop | Stop any active emission |
| GET | /v1/sessions | List available sessions |
| POST | /v1/sessions/start | Start an OSP session |
| POST | /v1/sessions/stop | Stop the active session |
| GET | /v1/status | Device status |
| GET | /v1/capabilities | Device capabilities |

### 4.2 POST /v1/emit — Example

**Request:**
```json
POST http://olfyn-device.local/v1/emit
Content-Type: application/json

{
  "scent_id": "personal_ana_001",
  "intensity_override": 0.60,
  "source": "mobile-app",
  "triggered_by": "pedro@email.com"
}
```

**Response 200 OK:**
```json
{
  "status": "emitting",
  "scent_id": "personal_ana_001",
  "started_at": "2026-06-01T14:32:00Z",
  "expected_end_at": "2026-06-01T14:35:00Z"
}
```

### 4.3 WebSocket — Real-Time Control

```
ws://olfyn-device.local/v1/stream
```

**Client → Device messages:**
```json
{ "action": "emit", "scent_id": "olfyn_lavanda_001", "intensity": 0.7 }
{ "action": "stop" }
{ "action": "session_start", "session_id": "therapy_alzheimer_001" }
{ "action": "session_stop" }
```

**Device → Client events:**
```json
{ "event": "emission_started", "scent_id": "olfyn_lavanda_001" }
{ "event": "emission_ended",   "scent_id": "olfyn_lavanda_001" }
{ "event": "session_step",     "step": 2, "scent_id": "olfyn_vainilla_001" }
{ "event": "error",            "code": "E003", "message": "Cartridge empty" }
```

---

## 5. Device Capabilities

Every OSP-compatible device must expose its capabilities:

```json
{
  "osp_version_supported": ["1.0"],
  "device_name": "OLFYN One",
  "device_id":   "olfyn-one-a3f2b1",
  "firmware":    "1.0.3",

  "actuators": {
    "count":     6,
    "type":      "liquid",
    "mechanism": "ultrasonic-mist",
    "slots": [
      { "id": 1, "dimension": "floral",    "filled": true  },
      { "id": 2, "dimension": "dulce",     "filled": true  },
      { "id": 3, "dimension": "leñoso",    "filled": true  },
      { "id": 4, "dimension": "animal",    "filled": true  },
      { "id": 5, "dimension": "frutal",    "filled": true  },
      { "id": 6, "dimension": "herbal",    "filled": false }
    ]
  },

  "transport": {
    "rest":      true,
    "websocket": true,
    "bluetooth": false
  },

  "features": {
    "sessions":      true,
    "fade":          true,
    "repeat":        true,
    "log_responses": false
  }
}
```

---

## 6. OLFYN DB

OLFYN DB is a public database of community-contributed OSP profiles.

### 6.1 Public API

| Endpoint | Description |
|---|---|
| GET api.olfyn.io/v1/db/profiles | Search and list profiles |
| GET api.olfyn.io/v1/db/profiles/{id} | Get profile by ID |
| POST api.olfyn.io/v1/db/profiles | Publish a profile (auth required) |
| GET api.olfyn.io/v1/db/profiles/{id}/similar | Find similar profiles |
| GET api.olfyn.io/v1/db/search?q=lavender | Search by name or tag |

### 6.2 Profile ID Prefixes

| Type | Prefix | Description |
|---|---|---|
| Official OLFYN | `olfyn_` | Validated by the OLFYN team |
| Personal | `personal_` | Private user profiles (not public) |
| Community | `comm_` | Community-contributed and verified |
| Therapeutic | `therapy_` | Clinically validated profiles |
| Experimental | `exp_` | Unverified, in testing |

---

## 7. Error Codes

| Code | Name | Description |
|---|---|---|
| E001 | INVALID_PROFILE | JSON does not conform to OSP v1.0 schema |
| E002 | UNKNOWN_SCENT_ID | scent_id not found on device or OLFYN DB |
| E003 | CARTRIDGE_EMPTY | Required scent slot is empty |
| E004 | DIMENSION_MISSING | Profile requires a dimension not available on device |
| E005 | ALREADY_EMITTING | Device is already emitting and not accepting new commands |
| E006 | SESSION_NOT_FOUND | Requested session_id does not exist |
| E007 | INTENSITY_OUT_OF_RANGE | Intensity value outside 0.0 – 1.0 range |
| E008 | DEVICE_NOT_READY | Device is initializing or in error state |
| E009 | VERSION_MISMATCH | OSP version in profile not supported by device |
| E010 | NETWORK_TIMEOUT | Device did not respond within timeout |

---

## 8. Certification

A device may declare itself **"OSP Compatible"** if it meets these minimum requirements:

1. Implements all REST endpoints marked as REQUIRED in section 4.1
2. Supports the full OSP object with all 10 aromatic dimensions
3. Correctly exposes GET /v1/capabilities
4. Handles and returns error codes E001 through E010
5. Supports at least 2 simultaneous active scent actuators

---

## 9. Versioning

OSP follows [Semantic Versioning](https://semver.org/):

- **MAJOR** (X.0) — Breaking changes
- **MINOR** (1.X) — New backwards-compatible features
- **PATCH** (1.0.X) — Specification bug fixes

---

## 10. Extensions

Any implementer may add proprietary fields using the `x-` prefix inside the `extensions` object. These fields are ignored by implementations that do not recognize them.

```json
{
  "osp_version": "1.0",
  "scent_id": "comm_coffee_espresso_001",
  "profile": { "ahumado": 0.25, "dulce": 0.10 },
  "intensity": 0.80,
  "duration_ms": 5000,
  "extensions": {
    "x-olfyn-therapy-level": "moderate",
    "x-olfyn-patient-age-range": "65-85"
  }
}
```

---

## 11. Governance

### License
MIT License — see [LICENSE](../LICENSE)

### Official Repository
[github.com/olfyn/olfyn-osp-spec](https://github.com/olfyn/olfyn-osp-spec)

### Change Process
1. **Proposal** — Anyone can propose changes via GitHub Issues
2. **Review** — OLFYN team and community review for 30 days
3. **Approval** — Approved changes are incorporated in the next MINOR or MAJOR version
4. **Publication** — New specification published with detailed changelog

---

*OSP v1.0 · OLFYN · June 2026 · MIT License · olfyn.io*
