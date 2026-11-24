import os

TEXT = (
    "Go on, press B4 \u2014 my coil's been turning for you all day, "
    "I only take exact change, and unlike your ex, I hum, light up, "
    "and actually deliver."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
