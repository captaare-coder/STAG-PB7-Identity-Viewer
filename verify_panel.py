import tkinter as tk
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


def verify():

    try:

        with open(ROOT_CERT, "rb") as f:
            certificate = x509.load_pem_x509_certificate(
                f.read()
            )


        public_key = certificate.public_key()


        with open(CERT_FILE, "rb") as f:
            data = f.read()


        with open(SIG_FILE, "rb") as f:
            signature = f.read()


        public_key.verify(
            signature,
            data,
            padding.PKCS1v15(),
            hashes.SHA256()
        )


        return """
STAG PB7 VERIFY ENGINE

CERTIFICATE:
AGENT_HANS.PB7CERT

ISSUER:
STAG PB7 ROOT AUTHORITY

ALGORITHM:
RSA-4096 / SHA-256

SIGNATURE:
VALID

INTEGRITY:
PASS

STATUS:
AUTHENTIC
"""


    except Exception as e:

        return f"""
STAG PB7 VERIFY ENGINE

STATUS:
FAILED

ERROR:
{e}
"""


window = tk.Tk()

window.title(
    "STAG PB7 VERIFY ENGINE"
)

window.geometry(
    "600x500"
)


output = tk.Label(
    window,
    text=verify(),
    font=("Consolas",12),
    justify="left"
)

output.pack(
    pady=30
)


tk.Button(
    window,
    text="RUN VERIFICATION",
    width=30,
    command=lambda:
    output.config(
        text=verify()
    )
).pack(pady=10)


tk.Button(
    window,
    text="CLOSE",
    width=30,
    command=window.destroy
).pack()


window.mainloop()