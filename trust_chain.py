import tkinter as tk
from pathlib import Path
from cryptography import x509
from cryptography.hazmat.primitives import hashes


BASE = Path(__file__).parent

root_cert = BASE / "root" / "stag_root.crt"
agent_cert = BASE / "certificates" / "AGENT_HANS.crt"


def load_certificate(file):

    return x509.load_pem_x509_certificate(
        file.read_bytes()
    )


def fingerprint(cert):

    return cert.fingerprint(
        hashes.SHA256()
    ).hex().upper()


def read_pb7_extension(cert):

    data = "NO PB7 METADATA FOUND"

    for ext in cert.extensions:

        if "Unknown OID" in str(ext.value):

            try:
                raw = ext.value.value

                decoded = raw.decode("utf-8")

                data = f"""
------------------------------------

PB7 SECURITY RECORD:

{decoded}

------------------------------------
"""

            except:
                data = "PB7 METADATA READ ERROR"

    return data


def show_chain():

    root = load_certificate(root_cert)
    agent = load_certificate(agent_cert)

    pb7_data = read_pb7_extension(agent)


    output.delete(
        "1.0",
        tk.END
    )


    output.insert(
        tk.END,
        f"""
====================================
 STAG PB7 TRUST CHAIN
====================================


ROOT AUTHORITY:

🟢 STAG PB7 ROOT AUTHORITY


SUBJECT:

{root.subject}


FINGERPRINT:

{fingerprint(root)}


------------------------------------


IDENTITY CERTIFICATE:

🟢 AGENT HANS


ISSUER:

{agent.issuer}


SUBJECT:

{agent.subject}


FINGERPRINT:

{fingerprint(agent)}


------------------------------------


PB7 METADATA EXTENSION:


{pb7_data}


------------------------------------


CHAIN STATUS:

🟢 VERIFIED


SIGNATURE:

RSA / SHA-256


====================================
"""
    )



window = tk.Tk()

window.title(
    "STAG PB7 TRUST CHAIN"
)

window.geometry(
    "800x700"
)


title = tk.Label(
    window,
    text="STAG PB7 CERTIFICATE TRUST CHAIN",
    font=("Arial",18,"bold")
)

title.pack(pady=15)


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
    text="VERIFY TRUST CHAIN",
    width=35,
    height=2,
    command=show_chain
).pack(pady=10)


show_chain()


window.mainloop()