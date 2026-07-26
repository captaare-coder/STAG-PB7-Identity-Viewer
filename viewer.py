from pathlib import Path

print("=" * 55)
print("        STAG PB7 CERTIFICATE VIEWER")
print("=" * 55)

folder = Path("certificates")

files = list(folder.glob("*.PB7CERT"))

if not files:
    print("No certificates found.")
    quit()

for i, f in enumerate(files, start=1):
    print(f"{i}. {f.name}")

choice = input("\nOpen certificate number: ")

try:
    selected = files[int(choice)-1]

    print("\n")
    print("=" * 55)
    print(selected.name)
    print("=" * 55)
    print(selected.read_text(encoding="utf-8"))

except:
    print("Invalid selection.")