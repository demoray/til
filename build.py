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

    with open("README.md", "w") as handle:
        print("# TIL (Today I learned)", file=handle)
        for tag in sorted(tags.keys()):
            print("## {}".format(tag), file=handle)
            for entry in sorted(tags[tag], key=lambda x: x["name"]):
                print("* [{}]({})".format(entry["name"], entry["path"]), file=handle)
            print("", file=handle)


if __name__ == "__main__":
    main()
