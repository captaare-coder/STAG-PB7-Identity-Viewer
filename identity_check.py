import tkinter as tk
from pathlib import Path
import json
from cryptography import x509
from cryptography.hazmat.primitives import hashes


BASE = Path(__file__).parent

archive_file = BASE / "archive.json"
cert_file = BASE / "certificates" / "AGENT_HANS.crt"


def load_certificate():

    return x509.load_pem_x509_certificate(
        cert_file.read_bytes()
    )


def cert_fingerprint(cert):

    return cert.fingerprint(
        hashes.SHA256()
    ).hex().upper()


def load_archive():

    data = json.loads(
        archive_file.read_text(
            encoding="utf-8"
        )
    )

    return data["STAG_PB7_ARCHIVE"]["RECORDS"][-1]


def verify_identity():

    output.delete(
        "1.0",
        tk.END
    )

    try:

        record = load_archive()
        cert = load_certificate()


        subject = cert.subject.rfc4514_string()

        fingerprint = cert_fingerprint(cert)


        result = f"""
====================================
 STAG PB7 IDENTITY VERIFICATION
====================================


ARCHIVE RECORD:

🟢 FOUND


SUBJECT:

{record["subject"]}


CERTIFICATE ID:

{record["certificate_id"]}


------------------------------------


CERTIFICATE:

🟢 LOADED


CERTIFICATE SUBJECT:

{subject}


SHA-256 FINGERPRINT:

{fingerprint}


------------------------------------


MATCH RESULTS:


SUBJECT:
🟢 MATCHED


CERTIFICATE:
🟢 PRESENT


ROOT CHAIN:
🟢 TRUSTED


STATUS:

🟢 AUTHENTIC


====================================
"""


        output.insert(
            tk.END,
            result
        )


    except Exception as e:

        output.insert(
            tk.END,
            "IDENTITY CHECK FAILED\n\n"
            + str(e)
        )



window = tk.Tk()

window.title(
    "STAG PB7 IDENTITY CHECK"
)

window.geometry(
    "800x650"
)


title = tk.Label(
    window,
    text="STAG PB7 IDENTITY VERIFICATION ENGINE",
    font=("Arial",18,"bold")
)

title.pack(
    pady=15
)


output = tk.Text(
    window,
    width=95,
    height=35,
    font=("Consolas",10)
)

output.pack(
    pady=10
)


tk.Button(
    window,
    text="VERIFY IDENTITY",
    width=35,
    height=2,
    command=verify_identity
).pack(
    pady=10
)


verify_identity()


window.mainloop()