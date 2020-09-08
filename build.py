#!/usr/bin/env python

import os
import glob


def main():
    tags = {}
    for path in glob.glob("**/*.md", recursive=True):
        if path in ["README.md"]:
            continue

        entries = path.split("/")
        filename = entries.pop()
        name = os.path.splitext(filename)[0].replace("-", " ").capitalize()
        for tag in entries:
            if tag not in tags:
                tags[tag] = []
            tags[tag].append({"path": path, "name": name})

    content = ['# TIL (Today I learned)']
    for tag in sorted(tags.keys()):
            content.append("## {}".format(tag.replace("-", " ")))
            for entry in sorted(tags[tag], key=lambda x: x["name"]):
                content.append("* [{}]({})".format(entry["name"], entry["path"]))
            content.append("")


    with open("README.md", "w") as handle:
        handle.write("\n".join(content))


if __name__ == "__main__":
    main()
