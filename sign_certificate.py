from pathlib import Path
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding


ROOT_KEY = Path("root/stag_root.key")

CERT_FILE = Path(
    "certificates/AGENT_HANS.PB7CERT"
)

SIGNATURE_FILE = Path(
    "certificates/AGENT_HANS.sig"
)


# Load private key

with open(ROOT_KEY, "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )


# Read PB7 certificate document

with open(CERT_FILE, "rb") as f:
    data = f.read()


# Create digital signature

signature = private_key.sign(
    data,
    padding.PKCS1v15(),
    hashes.SHA256()
)


# Save signature

with open(SIGNATURE_FILE, "wb") as f:
    f.write(signature)


print("=" * 45)
print(" STAG PB7 DIGITAL SIGNATURE CREATED ")
print("=" * 45)

print()
print("Certificate:")
print(CERT_FILE)

print()
print("Signature:")
print(SIGNATURE_FILE)

print()
print("Algorithm:")
print("RSA-4096 / SHA-256")

print()
print("STATUS: SUCCESS")