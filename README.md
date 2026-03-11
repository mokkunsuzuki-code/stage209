QSP Stage209 — Security Claim Matrix

QSP (Quantum Security Protocol) is a research-oriented project exploring the integration of modern cryptographic primitives and quantum-derived entropy sources within a transparent and verifiable session protocol architecture.

Stage209 introduces an explicit Security Claim Matrix, which links protocol assumptions to the security guarantees provided by the system.

This stage improves the transparency of the protocol's security reasoning by making the relationship between assumptions and guarantees explicit.

Purpose of Stage209

In cryptographic protocol analysis, it is critical to clearly define:

which assumptions the protocol relies on

which security guarantees follow from those assumptions

Stage209 introduces a structured mapping:

Assumption → Guarantee

This structure allows reviewers and researchers to understand how the protocol's security properties depend on specific cryptographic assumptions.

Security Claim Matrix

The Security Claim Matrix connects protocol assumptions with their corresponding guarantees.

Assumption	Description	Guarantees
A1	PQC shared secret unpredictability	Confidentiality
A2	HKDF pseudorandomness	Secure key derivation
A3	AES-GCM authenticated encryption	Message integrity and authenticity
A4	QKD entropy (optional)	Additional entropy source
A5	Fail-closed session enforcement	Safe protocol termination

The matrix makes the protocol’s trust boundaries explicit and prevents implicit or ambiguous security claims.

Project Evolution

Stage209 continues the architectural progression of the QSP protocol design.

Stage	Focus
Stage206	Protocol design
Stage207	Cryptographic integration
Stage208	Security model
Stage209	Security claim matrix

This progression gradually builds a clearer structure for protocol reasoning and security analysis.

Repository Structure
stage209
│
├ README.md
├ protocol_v1.0.md
│
├ docs
│   ├ security_assumptions.md
│   ├ threat_model.md
│   ├ guarantees.md
│   └ security_claims.md
│
├ qspcrypto
├ qsp_demo
├ scripts
└ tests
Documentation

The security documentation in this repository is organized as follows.

security_assumptions.md
Defines the assumptions required for protocol security.

threat_model.md
Describes the attacker capabilities considered in the design.

guarantees.md
Specifies the security guarantees provided by the protocol.

security_claims.md
Links assumptions to guarantees through the Security Claim Matrix.

Design Philosophy

The core idea of QSP is to separate:

Assumptions
Security properties
Protocol guarantees

This separation helps make the protocol's reasoning transparent and easier to review.

Rather than relying on implicit trust in cryptographic primitives, the protocol explicitly documents how each assumption contributes to the overall security guarantees.

Research Context

This repository is part of an ongoing exploration of protocol architectures that combine:

Post-Quantum Cryptography (PQC)

classical cryptographic primitives

optional quantum-derived entropy sources (QKD)

The aim is to study how these elements can be integrated into a session protocol while keeping the security reasoning explicit and reviewable.

License

MIT License
© 2025 Motohiro Suzuki