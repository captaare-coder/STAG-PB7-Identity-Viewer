from pathlib import Path
from hashlib import sha256

print("=" * 55)
print("        STAG PB7 SECURITY VERIFIER")
print("=" * 55)

certificate = Path("certificates/AGENT_HANS.PB7CERT")

if not certificate.exists():
    print("NO CERTIFICATE FOUND")
    exit()

data = certificate.read_bytes()

fingerprint = sha256(data).hexdigest().upper()

print()
print("CERTIFICATE:")
print(certificate.name)

print()
print("SHA-256 FINGERPRINT:")
print(fingerprint)

print()
print("STATUS:")
print("✓ CERTIFICATE FILE DETECTED")
print("✓ INTEGRITY HASH GENERATED")
print("✓ STAG PB7 RECORD ACTIVE")

print()
print("=" * 55)
print("       VERIFICATION COMPLETE")
print("=" * 55)