from pathlib import Path

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding


CERT_FILE = Path(
    "certificates/AGENT_HANS.PB7CERT"
)

SIG_FILE = Path(
    "certificates/AGENT_HANS.sig"
)

ROOT_CERT = Path(
    "root/stag_root.crt"
)


# Load public certificate

with open(ROOT_CERT, "rb") as f:
    certificate = x509.load_pem_x509_certificate(
        f.read()
    )


public_key = certificate.public_key()


# Load document

with open(CERT_FILE, "rb") as f:
    data = f.read()


# Load signature

with open(SIG_FILE, "rb") as f:
    signature = f.read()


print("=" * 45)
print(" STAG PB7 SIGNATURE VERIFICATION ")
print("=" * 45)

try:

    public_key.verify(
        signature,
        data,
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    print()
    print("SIGNATURE:")
    print("VALID")

    print()
    print("INTEGRITY:")
    print("PASS")

    print()
    print("STATUS:")
    print("AUTHENTIC")

except Exception:

    print()
    print("SIGNATURE:")
    print("FAILED")

    print()
    print("STATUS:")
    print("INVALID")