# Papers

This directory holds academic papers in arXiv format that come out of this project.
Each paper lives in its own folder, with LaTeX source, figures and a `build.sh`.

| Paper | Folder | Version | Status | Score |
|-------|--------|---------|--------|------:|
| The Case for an Objective Score for OER (OpenBook QR Score) | [openbook-qr-score](openbook-qr-score/) | 0.01 | position paper, built, not submitted | 90 (self-scored) |

## Building a paper

```bash
cd papers/<paper-folder>
./build.sh            # build main.pdf (requires: brew install tectonic)
./build.sh arxiv      # also create and test arxiv-upload.zip
./build.sh release    # also save a versioned copy of the PDF
./build.sh clean      # remove build artifacts
```

These papers were generated and scored with the `arxiv-paper-generator` skill.
