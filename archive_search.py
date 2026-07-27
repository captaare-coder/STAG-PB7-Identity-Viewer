import json
from pathlib import Path

print("=" * 55)
print("        STAG PB7 ARCHIVE SEARCH")
print("=" * 55)

archive_file = Path("archive.json")

if not archive_file.exists():
    print("ARCHIVE DATABASE NOT FOUND")
    exit()

archive = json.loads(
    archive_file.read_text(encoding="utf-8")
)

records = archive["STAG_PB7_ARCHIVE"]["RECORDS"]

query = input("\nSEARCH QUERY > ").upper()

print("\nSEARCHING STAG DATABASE...\n")

found = False

for record in records:

    searchable = (
        record["certificate_id"]
        + record["subject"]
        + record["field"]
        + record["clearance"]
    ).upper()

    if query in searchable:
        found = True

        print("=" * 55)
        print("RECORD FOUND")
        print("=" * 55)

        print("CERTIFICATE:")
        print(record["certificate_id"])

        print("\nSUBJECT:")
        print(record["subject"])

        print("\nFIELD:")
        print(record["field"])

        print("\nCLEARANCE:")
        print(record["clearance"])

        print("\nCREATED:")
        print(record["created"])

        print("\nFINGERPRINT:")
        print(record["fingerprint"])

        print("\nSTATUS:")
        print(record["status"])

        print("=" * 55)


if not found:
    print("NO MATCHING RECORDS FOUND")

print("\nSEARCH COMPLETE")