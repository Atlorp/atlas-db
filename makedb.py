#!/usr/bin/env python3

import json
import sys
import re
import logging
import os
from typing import List, Dict, Any

DB_FILENAME = "VENDS.txt"
DB_VERSION = 1
DB_DELIMITER = "\t"

UDB_FILE_PATH = os.path.join("docs", "data", "full.json")
PLATFORM = "nds"
REGION = "ANY"
LOG_FORMAT = "%(levelname)s: %(message)s"

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


def get_udb() -> List[Dict[str, Any]]:
    """Get UDB in json/list format."""
    try:
        if not os.path.exists(UDB_FILE_PATH):
            logging.error(f"Database file not found at {UDB_FILE_PATH}")
            sys.exit(1)

        with open(UDB_FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Failed to read database file: {e}")
        sys.exit(1)


def process_archive(app: Dict[str, Any], entry: Dict[str, Any]) -> None:
    """Add items to extract to an entry according to app's listed archives."""
    for archive_filename, archive_files in app["archive"].items():
        # Check if the archive's filename matches the entry's filename
        # archive_filename is a regular expression
        match = re.match(rf"{archive_filename}", entry["fileName"])

        if not match:
            continue

        groups = match.groups()

        for filename, files_to_extract in archive_files.items():
            # Skip .cia and .3dsx files as they are not needed
            if filename.endswith(".cia") or filename.endswith(".3dsx"):
                continue

            for file in files_to_extract:
                extract_item = {
                    # If the file is not a directory (doesn't end with '/'), format the filename with groups
                    # Otherwise, format the file itself with groups
                    "inPath": filename.format(*groups) if not file.endswith("/") else file.format(*groups),

                    # Always format the file with groups for outPath
                    "outPath": file.format(*groups)
                }
                entry["extractItems"].append(extract_item)
        break


def parse_udb(udb: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Parse UDB into a list of entries."""
    entries = []

    for app in udb:
        if "DS" not in app.get("systems", []):
            continue

        if "downloads" not in app or not app["downloads"]:
            continue

        entry = {
            "title": app.get("title", ""),
            "platform": PLATFORM,
            "region": REGION,
            "version": app.get("version", ""),
            "author": app.get("author", ""),
            "url": None,
            "fileName": None,
            "size": None,
            "boxartUrl": None,
            "extractItems": []
        }

        temp_downloads = []
        # Process downloads to find the appropriate file and URL
        # NDS files are usually in last position so the list is reversed
        for filename, download in reversed(list(app["downloads"].items())):
            temp_downloads.append({
                "filename": filename,
                "download": download
            })

            if "cia" in filename.lower() or "3ds" in filename.lower():
                continue

            if not filename.endswith(".zip") and not filename.endswith(".nds") and not filename.endswith(".dsi"):
                continue

            entry["url"] = download["url"]
            entry["size"] = download.get("size", 0)
            entry["fileName"] = filename
            break

        # If no file and URL was found, use the first download
        if not entry["url"]:
            entry["url"] = temp_downloads[0]["download"]["url"]
            entry["size"] = temp_downloads[0]["download"].get("size", 0)
            entry["fileName"] = temp_downloads[0]["filename"]

        if "archive" in app:
            process_archive(app, entry)

        entry["boxartUrl"] = app.get("image", app.get("icon", ""))

        entries.append(entry)

    return entries


def generate_db_content(entries: List[Dict[str, Any]]) -> str:
    """Generate the string content for the DB file."""
    lines = []
    lines.append(f"{DB_VERSION}")
    lines.append(f"{DB_DELIMITER}")

    for entry in entries:
        fields = [
            entry["title"],
            entry["platform"],
            entry["region"],
            entry["version"],
            entry["author"],
            entry["url"],
            entry["fileName"],
            str(entry["size"]),
            entry["boxartUrl"]
        ]

        for extract_item in entry["extractItems"]:
            fields.append(extract_item["inPath"])
            fields.append(extract_item["outPath"])

        lines.append(f"{DB_DELIMITER.join(fields)}")

    return "\n".join(lines) + "\n"


def make_db_file(entries: List[Dict[str, Any]]) -> None:
    """Create final DB file from a list of entries."""
    try:
        content = generate_db_content(entries)
        with open(DB_FILENAME, "w", encoding="utf-8", newline='\n') as f:
            f.write(content)
    except IOError as e:
        logging.error(f"Failed to write to file {DB_FILENAME}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    udb = get_udb()
    entries = parse_udb(udb)
    make_db_file(entries)
