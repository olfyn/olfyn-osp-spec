# Changelog

## [1.1.0] — 2026-07-01

### Added
- **Hybrid capture** (`POST /v1/capture`) — combines BME688 sensor + verbal description + AI synthesis
- **`capture` field** in OSP Profile object — documents creation method and source data
- **BME688 sensor support** — VOC-specific sensor replaces MQ kit in hardware reference
- **Confidence score** in capture response — indicates alignment between sensor data and verbal description
- **Two new profile categories** — `vinos` (wines) and `perfumeria` (perfumery)
- **E011, E012 error codes** — capture failure and sensor not connected
- **`sensors` field** in device capabilities — declares BME688 availability
- **`hybrid_capture` feature flag** in capabilities

### Changed
- Hardware reference updated: BME688 ($12) replaces MQ sensor kit ($12) — same cost, higher relevance for aromatics
- Total prototype cost updated to ~$80 (added base scent cartridges line item)
- Version bumped: `osp_version` now accepts `"1.0"` and `"1.1"`

### Removed
- MQ sensor kit from hardware reference (not suitable for aromatic compound detection)

### Rationale
MQ sensors were designed for industrial gas safety (butane, CO, methane detection). The BME688 was purpose-built for VOC detection and air quality — directly relevant to organic aromatic compounds that produce scents.

---

## [1.0.0] — 2026-06-01

### Added
- Initial OSP v1.0 specification
- 10 aromatic dimensions model
- Full OSP Profile JSON schema
- OSP Session structure
- REST API endpoint definitions
- WebSocket real-time protocol
- Device Capabilities format
- OLFYN DB public API
- Error codes E001–E010
- MIT License
