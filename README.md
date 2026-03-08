# Stage207: Crypto Integration Minimal (PQC + HKDF + AES-GCM, fail-closed)

This stage integrates minimal cryptographic components into the QSP prototype.

The goal is not to claim production security but to demonstrate a **minimal,
fail-closed cryptographic integration pipeline**.

## Architecture

PQC (stub)
+
QKD key
↓
HKDF-SHA256
↓
AES-256-GCM
↓
Authenticated encryption

If any required security input is missing, the system **fails closed**.

## Components

### qspcrypto

Minimal cryptographic integration layer.

Modules:

- `pqc_stub.py` – PQC KEM interface stub for integration testing
- `hkdf.py` – HKDF-SHA256 key derivation
- `aead.py` – AES-256-GCM authenticated encryption
- `session.py` – integration layer deriving AEAD keys
- `errors.py` – fail-closed exception definitions

### qsp_demo

Minimal protocol demonstration inherited from **Stage206**.

### tests

Security and functionality tests.

- `test_fail_closed.py` – verifies fail-closed behaviour
- `test_roundtrip.py` – AES-GCM encryption/decryption

## Run Tests

```bash
pip install -e .
pytest

Expected result

4 passed
Design Principle

This stage demonstrates:

minimal cryptographic wiring

explicit security preconditions

fail-closed behaviour

reproducible tests

The design goal is clarity of security boundaries rather than completeness.

License

MIT License
© 2025 Motohiro Suzuki
