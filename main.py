import os

LINE = "Exceeds expectations: assigns me every task, then presents my work as his leadership — promotion approved, authorship pending."


def main():
    assert 1 <= len(LINE) <= 140, len(LINE)
    assert LINE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
