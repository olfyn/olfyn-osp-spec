# OSP v1.1 Profile Examples

## 1. Hybrid Capture — Memory (Alzheimer)

Created with BME688 sensor + verbal description + AI synthesis.

```json
{
  "osp_version": "1.1",
  "scent_id": "memoria_jardin_mama_a3f2",
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
      "temperature":   22.5,
      "humidity":      61.0,
      "dominant_note": "floral",
      "volatility":    "medium"
    },
    "verbal_description": "El jardín de mamá. Lavanda, algo de tierra húmeda y flores que no sé cómo se llaman.",
    "ai_model":   "claude-haiku-4-5",
    "confidence": 0.74
  },
  "metadata": {
    "category": "memoria",
    "person":   "Mamá",
    "tags":     ["alzheimer", "memoria", "jardín", "terapia"]
  }
}
```

---

## 2. Hybrid Capture — Presence (Long Distance Couple)

```json
{
  "osp_version": "1.1",
  "scent_id": "presencia_ana_firma_b7c3",
  "name": "La presencia de Ana",
  "created_at": "2026-07-01T14:20:00Z",
  "profile": {
    "animal":    0.40,
    "floral":    0.28,
    "leñoso":    0.15,
    "dulce":     0.12,
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
  "capture": {
    "method": "hybrid",
    "sensor_data": {
      "voc_index":     198,
      "dominant_note": "animal",
      "volatility":    "low"
    },
    "verbal_description": "Su perfume. Algo almizclado, una flor suave y madera. Muy sutil.",
    "ai_model":   "claude-haiku-4-5",
    "confidence": 0.81
  },
  "metadata": {
    "category": "presencia",
    "person":   "Ana",
    "tags":     ["pareja", "distancia", "firma-personal"]
  }
}
```

---

## 3. Predefined — Wine (Cabernet Sauvignon)

No sensor needed — chemistry documented by enologists.

```json
{
  "osp_version": "1.1",
  "scent_id": "olfyn_vino_cabernet_001",
  "name": "Cabernet Sauvignon",
  "description": "Full-bodied red. Dark fruits, cedar, soft tannins, vanilla finish.",
  "author": "OLFYN",
  "created_at": "2026-07-01T00:00:00Z",
  "profile": {
    "frutal":    0.40,
    "leñoso":    0.25,
    "especiado": 0.15,
    "animal":    0.10,
    "dulce":     0.05,
    "ahumado":   0.05,
    "floral":    0.00,
    "herbal":    0.00,
    "marino":    0.00,
    "químico":   0.00
  },
  "intensity":   0.70,
  "duration_ms": 12000,
  "fade_in_ms":  1000,
  "fade_out_ms": 2000,
  "capture": {
    "method": "predefined"
  },
  "metadata": {
    "category": "vinos",
    "tags": ["red", "full-bodied", "oak", "cabernet"]
  }
}
```

---

## 4. Predefined — Perfumery (Oriental Woody)

```json
{
  "osp_version": "1.1",
  "scent_id": "olfyn_perfume_oriental_001",
  "name": "Oriental Amaderado",
  "description": "Warm spices, oud, sandalwood and amber. Sensual and mysterious.",
  "author": "OLFYN",
  "created_at": "2026-07-01T00:00:00Z",
  "profile": {
    "especiado": 0.35,
    "leñoso":    0.30,
    "animal":    0.20,
    "dulce":     0.10,
    "ahumado":   0.05,
    "floral":    0.00,
    "frutal":    0.00,
    "herbal":    0.00,
    "marino":    0.00,
    "químico":   0.00
  },
  "intensity":   0.70,
  "duration_ms": 20000,
  "fade_in_ms":  3000,
  "fade_out_ms": 6000,
  "capture": {
    "method": "predefined"
  },
  "metadata": {
    "category": "perfumeria",
    "tags": ["oriental", "oud", "night", "sensual"]
  }
}
```

---

## 5. Therapy Session — Alzheimer 20-minute Protocol

```json
{
  "osp_version":       "1.1",
  "session_id":        "therapy_alzheimer_20min_001",
  "session_name":      "Alzheimer Memory Therapy — 20 min",
  "category":          "memoria",
  "total_duration_ms": 1200000,
  "sequence": [
    {
      "offset_ms": 0,
      "scent_id":  "olfyn_lavanda_memoria_001",
      "intensity_override": 0.50,
      "label":     "Calming opening"
    },
    {
      "offset_ms": 300000,
      "scent_id":  "olfyn_vainilla_hogar_001",
      "label":     "Home and warmth memory"
    },
    {
      "offset_ms": 600000,
      "scent_id":  "memoria_jardin_mama_a3f2",
      "label":     "Personal family memory"
    },
    {
      "offset_ms": 900000,
      "scent_id":  "olfyn_lavanda_memoria_001",
      "intensity_override": 0.30,
      "label":     "Gentle closing"
    }
  ],
  "log_responses": true,
  "metadata": {
    "notes": "Standard 20-minute Alzheimer olfactory stimulation protocol"
  }
}
```
