
import hashlib
from datetime import datetime
from pathlib import Path


def calculate_hashes(file_path):
    """Calculate file hashes without loading the entire file into memory."""

    hashes = {
        "MD5": hashlib.md5(),
        "SHA-1": hashlib.sha1(),
        "SHA-256": hashlib.sha256()
    }

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(1024 * 1024)

            if not chunk:
                break

            for hasher in hashes.values():
                hasher.update(chunk)

    return {
        name: hasher.hexdigest()
        for name, hasher in hashes.items()
    }


def verify_sha256(file_path, original_hash):
    """Compare current SHA-256 with a previously recorded hash."""

    current_hash = calculate_hashes(file_path)["SHA-256"]

    is_match = current_hash.lower() == original_hash.strip().lower()

    return is_match, current_hash


def main():

    print("\nDIGITAL FORENSICS HASH TOOL")
    print("=" * 30)
    print("1. Calculate hashes and generate report")
    print("2. Verify SHA-256 against a recorded hash")

    choice = input("\nSelect an option (1 or 2): ").strip()

    if choice not in ("1", "2"):
        print("Invalid option. Please select 1 or 2.")
        return

    file_path = Path(
        input("Enter the path to the file: ").strip().strip('"')
    )

    try:

        if not file_path.is_file():
            print("Error: The path does not point to a regular file.")
            return

        file_size = file_path.stat().st_size
        hashes = calculate_hashes(file_path)

        if choice == "2":

            original_hash = input(
                "Enter the previously recorded SHA-256: "
            ).strip()

            if len(original_hash) != 64 or any(
                character not in "0123456789abcdefABCDEF"
                for character in original_hash
            ):
                print("Error: Enter a valid 64-character SHA-256 hash.")
                return

            is_match, current_hash = verify_sha256(
                file_path, original_hash
            )

            print("\nSHA-256 VERIFICATION RESULT")
            print("=" * 30)
            print(f"Recorded hash: {original_hash}")
            print(f"Current hash:  {current_hash}")

            if is_match:
                print("RESULT: MATCH - file data matches the recorded hash.")
            else:
                print("RESULT: MISMATCH - file data differs from the recorded hash.")

            return

        timestamp = datetime.now().astimezone().isoformat(
            timespec="seconds"
        )

        report_dir = Path("reports")
        report_dir.mkdir(exist_ok=True)

        report_name = (
            "hash_report_"
            + datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            + ".txt"
        )

        report_path = report_dir / report_name

        report_lines = [
            "DIGITAL EVIDENCE HASH REPORT",
            "=" * 32,
            f"File name: {file_path.name}",
            f"File path: {file_path.resolve()}",
            f"File size: {file_size} bytes",
            f"Report generated: {timestamp}",
            "",
            "HASH VALUES",
            "-" * 32,
            f"MD5:     {hashes['MD5']}",
            f"SHA-1:   {hashes['SHA-1']}",
            f"SHA-256: {hashes['SHA-256']}",
            "",
            "Note: This report records calculated hash values.",
            "It does not independently establish the file's",
            "origin, authenticity, or chain of custody."
        ]

        report_text = "\n".join(report_lines) + "\n"

        report_path.write_text(report_text, encoding="utf-8")

        print("\n" + report_text)
        print(f"Report saved to: {report_path}")

    except FileNotFoundError:
        print("Error: The file was not found.")

    except PermissionError:
        print("Error: Permission denied while accessing the file.")

    except OSError as error:
        print(f"File operation failed: {error}")


if __name__ == "__main__":
    main()
