from pathlib import Path
from datetime import datetime, timedelta

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa


# ----------------------------------------
# Output Folder
# ----------------------------------------

ROOT = Path("root")
ROOT.mkdir(exist_ok=True)


# ----------------------------------------
# Generate RSA Private Key
# ----------------------------------------

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=4096
)


# ----------------------------------------
# Subject / Issuer
# ----------------------------------------

subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "NZ"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Bay of Plenty"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "Rotorua"),
    x509.NameAttribute(
        NameOID.ORGANIZATION_NAME,
        "Strategic Technology & Access Group"
    ),
    x509.NameAttribute(
        NameOID.ORGANIZATIONAL_UNIT_NAME,
        "PB7 Security Division"
    ),
    x509.NameAttribute(
        NameOID.COMMON_NAME,
        "STAG PB7 Root Authority"
    ),
])


# ----------------------------------------
# Build Certificate
# ----------------------------------------

certificate = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(private_key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(
        datetime.utcnow() + timedelta(days=3650)
    )
    .add_extension(
        x509.BasicConstraints(ca=True, path_length=None),
        critical=True,
    )
    .sign(
        private_key,
        hashes.SHA256()
    )
)


# ----------------------------------------
# Save Private Key
# ----------------------------------------

with open(ROOT / "stag_root.key", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    )


# ----------------------------------------
# Save Certificate
# ----------------------------------------

with open(ROOT / "stag_root.crt", "wb") as f:
    f.write(
        certificate.public_bytes(
            serialization.Encoding.PEM
        )
    )


print("=" * 40)
print(" STAG PB7 ROOT CERTIFICATE CREATED")
print("=" * 40)
print()
print("Private Key:")
print(ROOT / "stag_root.key")
print()
print("Certificate:")
print(ROOT / "stag_root.crt")
print()
print("SUCCESS")