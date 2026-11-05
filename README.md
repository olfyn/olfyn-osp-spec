# OLFYN — Open Scent Protocol (OSP)

> *"El estándar abierto para transmitir olores en digital."*
> *The open standard for digital scent transmission.*

**Creador:** Franklin Rodriguez · Ciudad de Panamá
**Versión actual:** OSP v1.1 (borrador) · **Licencia:** MIT

---

## Qué es

La vista se digitalizó con la fotografía, el sonido con el audio y el tacto con la háptica. **El olfato todavía no.**

OSP es un estándar abierto para **describir, transmitir y reproducir olores**. Hace con el olor lo que RGB hace con el color: cualquier aroma se describe como una combinación de **10 dimensiones aromáticas**, cada una de 0.0 a 1.0, y viaja entre dispositivos como JSON por REST o WebSocket.

```
floral · frutal · herbal · leñoso · ahumado · especiado · animal · químico · marino · dulce
```

## Para qué: los casos más humanos primero

| Perfil | Caso de uso |
|---|---|
| 🧠 **Memoria** | Terapia olfativa para personas con Alzheimer |
| 💑 **Presencia** | Compartir el olor de alguien a distancia |
| 🕊️ **Recuerdo** | Preservar el olor de alguien que ya no está |
| 🍷 **Sommelier** | Aromas de vino a distancia |
| 💐 **Perfumería** | Probar un perfume antes de comprarlo en línea |

## Cómo se crea un perfil: captura híbrida (v1.1)

1. Un **sensor BME688** lee el objeto (una prenda, unas flores…): índice de compuestos volátiles, volatilidad, temperatura y humedad.
2. La persona **lo describe con sus palabras**: *"Lavanda, algo de tierra húmeda…"*.
3. Una **IA combina ambas fuentes** y genera el perfil de 10 dimensiones, con un índice de confianza.
4. La persona **lo ajusta** con controles deslizantes y lo guarda.

Ejemplo real de la especificación: *"El jardín de mamá"*, un perfil de categoría memoria creado por captura híbrida.

## Qué define la especificación

- Modelo de datos del perfil OSP y JSON Schema para validarlo.
- Sesiones (intensidad, duración, entrada y salida gradual del aroma).
- API REST, eventos WebSocket y endpoint de captura `POST /v1/capture`.
- Capacidades de dispositivo, base de perfiles OLFYN DB, códigos de error, certificación, versionado y gobernanza.

## Hardware de referencia

Prototipo estimado en **~80 USD**: Raspberry Pi Zero 2W, sensor BME688, difusor ultrasónico, Arduino Nano, Bluetooth HC-05 y 6 cartuchos de aromas base. Detalle en la especificación.

## Estado

| | |
|---|---|
| Especificación | **v1.1 publicada como borrador** (v1.0 en junio de 2026; v1.1 en julio de 2026) |
| Código de referencia | Aún no existe en este repositorio |
| Prototipo físico | Lista de materiales definida; sin evidencia de construcción en este repositorio |
| Próximas versiones | OSP 1.2 (sesiones adaptativas, Q1 2027) · OSP 2.0 (firmas personales cifradas, 2028) |

## Documentación

| Documento | v1.1 (actual) | v1.0 |
|---|---|---|
| Presentación | [README](olfyn-osp-spec-v1.1/olfyn-osp-spec-v1.1/README.md) | [README](olfyn-osp-spec/olfyn-osp-spec/README.md) |
| Especificación técnica | [SPECIFICATION.md](olfyn-osp-spec-v1.1/olfyn-osp-spec-v1.1/SPECIFICATION.md) | [SPECIFICATION.md](olfyn-osp-spec/olfyn-osp-spec/SPECIFICATION.md) |
| JSON Schema | [osp-profile-v1.1.json](olfyn-osp-spec-v1.1/olfyn-osp-spec-v1.1/schema/osp-profile-v1.1.json) | [osp-profile-v1.0.json](olfyn-osp-spec/olfyn-osp-spec/schema/osp-profile-v1.0.json) |
| Ejemplos (5 categorías) | [EXAMPLES.md](olfyn-osp-spec-v1.1/olfyn-osp-spec-v1.1/examples/EXAMPLES.md) | [EXAMPLES.md](olfyn-osp-spec/olfyn-osp-spec/examples/EXAMPLES.md) |
| Historial de cambios | [CHANGELOG.md](olfyn-osp-spec-v1.1/olfyn-osp-spec-v1.1/CHANGELOG.md) | [CHANGELOG.md](olfyn-osp-spec/olfyn-osp-spec/CHANGELOG.md) |

La especificación técnica está en inglés para facilitar su adopción internacional.

## Licencia

MIT. Ver [LICENSE](olfyn-osp-spec-v1.1/olfyn-osp-spec-v1.1/LICENSE).
