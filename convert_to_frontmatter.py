#!/usr/bin/env python3

import json
import re
import os.path
import sys
from collections import OrderedDict

def row_to_md(row):
    md = ""
    if row.get("link","") != "":
        md += "[{}]({})".format(row["name"], row["link"])
    # for key, value in row:
    #     if key in ["name", "link", "id", "_xml", "_links"]:
    #         continue
    #     md += '<span>{}</span>'.format(value)
    if "text" in row:
        md += row["text"]
    md += "\n\n"
    return md


infile = sys.argv[1]
rows = []

print("reading", infile)
with open(infile) as f:
    rows = json.load(f)["rows"]
    print(len(rows), "rows")

sections = OrderedDict()
body = ""
items = []

for row in rows:
    del row["id"]
    del row["_xml"]
    del row["_links"]
    del row["title"]

    # if row['projecttitle'] == '':
    #     body += row['summary'] + "\n\n"
    #     continue


    # if row['title'] == '':
    #     body += row['fulltext'] + "\n\n"
    #     continue

    section = row.get("section", "")
    if section == '' and 'text' in row:
        body += row_to_md(row)
        continue

    del row["section"]
    if not section in sections:
        print("creating section", section)
        sections[section] = []

    sections[section].append(row)

    items.append(row)

for title, section in sections.items():
    if section[0].get("link", "") != "":
        body += "### {}\n\n".format(title)
        for item in section:
            body += row_to_md(item)

data = {
    "title": infile.replace(".json", "").replace("-", " ").title(),
    "path": infile.replace(".json", ""),
    "sections": sections
    # "items": items
}
outfile = infile.replace(".json", ".md")
with open(outfile, "w") as of:
    of.write("---\n")
    for key, value in data.items():
        print("writing section", key)
        of.write(key)
        of.write(": ")
        of.write(json.dumps(value))
        of.write("\n")
    of.write("---\n")
    of.write(body)
