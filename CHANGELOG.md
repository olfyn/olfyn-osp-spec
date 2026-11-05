# Changelog

## [Unreleased]

### Added
- Reference profile validator (`tools/validate.py`) and CI that validates the examples
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` and issue templates
- Health and safety notice (spec §1.3): OSP makes no therapeutic or clinical claims

### Changed
- Repository layout: v1.1 at the root, v1.0 under `versions/v1.0/`
- README rewritten in English
- Health-related wording in the spec and examples no longer implies clinical validation
- Repository links point to github.com/olfyn/olfyn-osp-spec
- Removed references to the `olfyn.io` domain, which the project does not own: schema `$id`s now point to this repository, and v1.0's OLFYN DB host is a `{OLFYN_DB_HOST}` placeholder

### Fixed
- README quick example was missing the required `created_at` field

---

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
