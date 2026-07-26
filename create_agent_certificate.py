from cryptography import x509
from cryptography.x509.oid import NameOID, ObjectIdentifier
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta
from pathlib import Path


BASE = Path(__file__).parent

root_cert_file = BASE / "root" / "stag_root.crt"
root_key_file = BASE / "root" / "stag_root.key"

output = BASE / "certificates" / "AGENT_HANS.crt"


# Load root certificate
root_cert = x509.load_pem_x509_certificate(
    root_cert_file.read_bytes()
)

# Load root private key
root_key = serialization.load_pem_private_key(
    root_key_file.read_bytes(),
    password=None
)


subject = issuer = x509.Name([
    x509.NameAttribute(
        NameOID.COMMON_NAME,
        "AGENT HANS"
    ),
    x509.NameAttribute(
        NameOID.ORGANIZATIONAL_UNIT_NAME,
        "PB7 Security Division"
    ),
    x509.NameAttribute(
        NameOID.ORGANIZATION_NAME,
        "Strategic Technology & Access Group"
    ),
    x509.NameAttribute(
        NameOID.COUNTRY_NAME,
        "NZ"
    )
])


builder = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(root_cert.subject)
    .public_key(root_key.public_key())
    .serial_number(
        x509.random_serial_number()
    )
    .not_valid_before(
        datetime.utcnow()
    )
    .not_valid_after(
        datetime.utcnow()
        + timedelta(days=3650)
    )
)


# STAG custom metadata

builder = builder.add_extension(
    x509.UnrecognizedExtension(
        ObjectIdentifier("1.3.6.1.4.1.99999.1"),
        b"""
STAG-PB7-TS7-204122045154
LEVEL 7
AGENT HANS
AUTHORIZED
"""
    ),
    critical=False
)


certificate = builder.sign(
    private_key=root_key,
    algorithm=hashes.SHA256()
)


output.write_bytes(
    certificate.public_bytes(
        serialization.Encoding.PEM
    )
)


print("==============================")
print(" STAG PB7 AGENT CERT CREATED")
print("==============================")
print()
print(output)
print()
print("ISSUER:")
print(certificate.issuer)
print()
print("SUBJECT:")
print(certificate.subject)
print()
print("STATUS: SUCCESS")