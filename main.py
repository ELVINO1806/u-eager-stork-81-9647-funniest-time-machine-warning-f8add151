import os


def build_entry():
    label = "CAUTION: "
    body = "Passengers from the future are asked not to correct the pilot."
    twist = " He is you."
    return label + body + twist


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(build_entry())


if __name__ == "__main__":
    main()
