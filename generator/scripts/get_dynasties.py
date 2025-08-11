import os
import re

COUNTRIES_PATH = (
    "/mnt/data/SteamLibrary/steamapps/common/Europa Universalis IV/history/countries"
)

# Regex patterns
religion_pattern = re.compile(r"religion\s*=\s*(sunni|shiite|ibadi)")
dynasty_pattern = re.compile(
    r'\bmonarch\s*=\s*\{[^{}]*?dynasty\s*=\s*"([^"]+)"[^{}]*?\}', re.DOTALL
)

dynasties = set()

for filename in os.listdir(COUNTRIES_PATH):
    if not filename.endswith(".txt"):
        continue

    filepath = os.path.join(COUNTRIES_PATH, filename)
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Skip files without the desired religion
    if not religion_pattern.search(content):
        continue

    # Find all monarch blocks with dynasties
    matches = dynasty_pattern.findall(content)
    dynasties.update(matches)

# Output the results
for dynasty in sorted(dynasties):
    print(dynasty)
