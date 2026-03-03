# Stage206: Spec-Consistent Minimal Demo (Fail-Closed)

MIT License © 2025 Motohiro Suzuki

## Purpose
Stage206 proves:

- It follows protocol_v1.0.md (Stage205 frozen spec)
- State machine matches allowed transitions
- Wire format is validated
- Fail-closed actually happens

## Run demo
python -m scripts.run_demo

## Run tests
pytest -q
