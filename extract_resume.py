import sys
from pathlib import Path

try:
    from pdfminer.high_level import extract_text
except Exception as e:
    print("Missing dependency: pdfminer.six. Please install it with: pip install pdfminer.six", file=sys.stderr)
    raise


def main():
    project_dir = Path(__file__).resolve().parent
    pdf_path = project_dir / "Resume 5.pdf"
    out_path = project_dir / "resume_extracted.txt"

    if not pdf_path.exists():
        print(f"PDF not found at: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    # Extract text
    text = extract_text(str(pdf_path)) or ""

    # Normalize whitespace a bit
    normalized = "\n".join(line.strip() for line in text.splitlines() if line.strip())

    out_path.write_text(normalized, encoding="utf-8")
    print(f"Wrote extracted text to: {out_path}")


if __name__ == "__main__":
    main()
