#!/usr/bin/env python3
"""Update Workbench all-releases.json with a new release entry."""

import argparse
import json
from datetime import date
import urllib.error
import urllib.request

EXPIRY_MONTHS = 18


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', required=True)
    parser.add_argument('--pub-date', required=True)
    parser.add_argument('--url', required=True)
    parser.add_argument('--sha256hash', required=True)
    parser.add_argument('--docs-url', required=True)
    parser.add_argument('--existing-url', required=True, help='CDN URL of existing all-releases.json')
    parser.add_argument('--output', required=True)
    parser.add_argument('--dry-run', action='store_true', help='Print output to stdout instead of writing file')
    args = parser.parse_args()

    # Download existing releases (or start fresh)
    try:
        with urllib.request.urlopen(args.existing_url) as response:
            existing = json.loads(response.read().decode()).get('releases', [])
        print(f"Downloaded {len(existing)} existing releases from {args.existing_url}")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            existing = []
            print(f"No existing releases found (starting fresh): {e}")
        else:
            raise

    # Create new entry
    new_entry = {
        'version': args.version,
        'pub_date': args.pub_date,
        'url': args.url,
        'sha256hash': args.sha256hash,
        'docs_url': args.docs_url,
    }

    # Remove existing entry with same year and month only if new version has a newer patch
    version_month = '.'.join(args.version.split('.')[:2])
    new_patch = int(args.version.split('.')[2].split('-')[0])

    existing_same_month = next(
        (r for r in existing if '.'.join(r.get('version', '').split('.')[:2]) == version_month), None
    )
    if existing_same_month is not None:
        try:
            existing_patch = int(existing_same_month['version'].split('.')[2].split('-')[0])
        except (IndexError, ValueError, KeyError):
            existing_patch = -1
        if new_patch < existing_patch:
            print(f"Skipping: existing version {existing_same_month['version']} has a newer patch than {args.version}")
            return

    releases = [r for r in existing if '.'.join(r.get('version', '').split('.')[:2]) != version_month]
    releases.append(new_entry)

    # Filter: only keep releases within 18 months
    total_months = date.today().year * 12 + date.today().month - EXPIRY_MONTHS
    cutoff = date(total_months // 12, total_months % 12 or 12, 1)

    def parse_version_date(version_str):
        parts = version_str.split('.')
        try:
            return date(int(parts[0]), int(parts[1]), 1)
        except (ValueError, IndexError, TypeError):
            return date.max

    filtered = [r for r in releases if parse_version_date(r.get('version', '')) >= cutoff]
    removed_count = len(releases) - len(filtered)
    if removed_count > 0:
        print(f"Filtered out {removed_count} releases older than {EXPIRY_MONTHS} months")

    # Sort by version descending
    filtered.sort(key=lambda r: r.get('version', ''), reverse=True)

    output_data = {'releases': filtered}

    if args.dry_run:
        print(f"\n--- DRY RUN: Would write {len(filtered)} releases to {args.output} ---")
        print(json.dumps(output_data, indent=2))
    else:
        with open(args.output, 'w') as f:
            json.dump(output_data, f, indent=2)
        print(f"Wrote {len(filtered)} releases to {args.output}")


if __name__ == '__main__':
    main()
