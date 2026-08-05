# OSP Profile Examples

## 1. Lavender from mom's garden (Memory — Alzheimer)

```json
{
  "osp_version": "1.0",
  "scent_id": "olfyn_lavanda_hogar_001",
  "name": "Lavender from mom's garden",
  "description": "French lavender, slightly herbal, from childhood garden",
  "created_at": "2026-06-01T00:00:00Z",
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
    "person":   "Mamá",
    "tags":     ["alzheimer", "memory", "garden", "childhood"],
    "language": "es"
  }
}
```

---

## 2. Ana's personal scent signature (Presence — Long Distance)

```json
{
  "osp_version": "1.0",
  "scent_id": "personal_ana_firma_001",
  "name": "Ana's Presence",
  "description": "Personal scent signature — soft musk with floral and wood notes",
  "created_at": "2026-06-01T00:00:00Z",
  "profile": {
    "animal":    0.40,
    "floral":    0.30,
    "leñoso":    0.15,
    "dulce":     0.10,
    "especiado": 0.05,
    "herbal":    0.00,
    "frutal":    0.00,
    "ahumado":   0.00,
    "marino":    0.00,
    "químico":   0.00
  },
  "intensity":   0.55,
  "duration_ms": 180000,
  "fade_in_ms":  3000,
  "fade_out_ms": 8000,
  "metadata": {
    "category": "presencia",
    "person":   "Ana",
    "tags":     ["long-distance", "partner", "personal-signature"],
    "language": "es"
  }
}
```

---

## 3. Espresso (General — Café La Suerte)

```json
{
  "osp_version": "1.0",
  "scent_id": "olfyn_espresso_001",
  "name": "Double Espresso",
  "description": "Dark roast, intense, slightly smoky with caramel undertones",
  "created_at": "2026-06-01T00:00:00Z",
  "profile": {
    "ahumado":   0.25,
    "dulce":     0.20,
    "herbal":    0.15,
    "leñoso":    0.15,
    "especiado": 0.10,
    "frutal":    0.10,
    "floral":    0.05,
    "animal":    0.00,
    "marino":    0.00,
    "químico":   0.00
  },
  "intensity":   0.80,
  "duration_ms": 5000,
  "fade_in_ms":  500,
  "fade_out_ms": 1000,
  "metadata": {
    "category": "general",
    "tags":     ["coffee", "espresso", "food-beverage"],
    "language": "en"
  }
}
```

---

## 4. Therapy Session — Alzheimer Memory Protocol

```json
{
  "osp_version":       "1.0",
  "session_id":        "therapy_alzheimer_standard_001",
  "session_name":      "Alzheimer Memory Therapy — Standard 20min",
  "created_at":        "2026-06-01T00:00:00Z",
  "category":          "therapy",
  "total_duration_ms": 1200000,
  "sequence": [
    {
      "offset_ms": 0,
      "scent_id":  "olfyn_lavanda_hogar_001",
      "intensity_override": 0.50,
      "label":     "Calming opening"
    },
    {
      "offset_ms": 300000,
      "scent_id":  "olfyn_vainilla_001",
      "label":     "Home and warmth memory"
    },
    {
      "offset_ms": 600000,
      "scent_id":  "personal_mom_garden",
      "label":     "Personal family memory"
    },
    {
      "offset_ms": 900000,
      "scent_id":  "olfyn_lavanda_hogar_001",
      "intensity_override": 0.30,
      "label":     "Gentle closing"
    }
  ],
  "log_responses": true,
  "metadata": {
    "category":  "memoria",
    "notes":     "Standard 20-minute Alzheimer olfactory stimulation protocol"
  }
}
```
