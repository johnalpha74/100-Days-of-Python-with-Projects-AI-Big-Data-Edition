import csv
import json
import re

def clean_text(text):
    text = text.lower()                     # normalize case
    text = re.sub(r'[^\w\s]', '', text)     # remove punctuation
    return text.strip()

# Step 1: Read CSV & clean reviews
cleaned_data = []
with open("reviews.csv", "r", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        cleaned_data.append({
            "review_id": row["review_id"],
            "cleaned_review": clean_text(row["review_text"])
        })

# Step 2: Write cleaned reviews to CSV
with open("clean_reviews.csv", "w", newline="", encoding="utf-8") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=["review_id", "cleaned_review"])
    writer.writeheader()
    writer.writerows(cleaned_data)

# Step 3: Export to JSON
with open("clean_reviews.json", "w", encoding="utf-8") as jsonfile:
    json.dump(cleaned_data, jsonfile, indent=4)
