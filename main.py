import os

LINE = "My GPS sighed before recalculating today. I didn't miss a turn, it's just disappointed in my life choices."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)

if __name__ == "__main__":
    main()
