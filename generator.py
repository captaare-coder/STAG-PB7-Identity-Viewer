import json
from pathlib import Path
from hashlib import sha256
from datetime import datetime
import uuid

agent = "AGENT HANS"
field = "204122045154"
clearance = "LEVEL 7"

certificate_id = f"STAG-PB7-{uuid.uuid4().hex[:12].upper()}"

created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

fingerprint = sha256(
    f"{agent}{field}{certificate_id}{created}".encode()
).hexdigest().upper()

certificate = f"""
-----BEGIN STAG PB7CERT-----

STAG GALACTIC ARCHIVE
PB7 ROOT TRUST RECORD

Certificate ID:
{certificate_id}

Subject:
{agent}

Field:
{field}

Clearance:
{clearance}

Created:
{created}

Fingerprint (SHA-256):
{fingerprint}

Status:
AUTHORIZED

-----END STAG PB7CERT-----
"""

output_dir = Path("certificates")
output_dir.mkdir(exist_ok=True)

filename = output_dir / "AGENT_HANS.PB7CERT"

filename.write_text(certificate, encoding="utf-8")

archive_file = Path("archive.json")

record = {
    "certificate_id": certificate_id,
    "subject": agent,
    "field": field,
    "clearance": clearance,
    "created": created,
    "fingerprint": fingerprint,
    "status": "ACTIVE"
}
from stag_log import log_event
if archive_file.exists():
    archive = json.loads(archive_file.read_text())
else:
    archive = {
        "STAG_PB7_ARCHIVE": {
            "VERSION": "7.0",
            "STATUS": "ACTIVE",
            "RECORDS": []
        }
    }

archive["STAG_PB7_ARCHIVE"]["RECORDS"].append(record)

archive_file.write_text(
    json.dumps(archive, indent=4),
    encoding="utf-8"
)

print("ARCHIVE STATUS: RECORD ADDED")

log_event(
    "CERTIFICATE CREATED: " + certificate_id
)

print("=================================")
print(" STAG PB7 CERTIFICATE GENERATED ")
print("=================================")
print(filename.resolve())