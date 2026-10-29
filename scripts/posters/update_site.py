#!/usr/bin/env python3
"""Add the overlay posters to the site: the Posters nav section in mkdocs.yml and the gallery in docs/posters/index.md.

Safe to run again. It only inserts what is missing, and it rewrites only the block between the two
gallery marker comments in docs/posters/index.md. Other posters listed on those pages are left alone.

    python3 scripts/posters/update_site.py
"""
import html
import importlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / 'specs'))
from build_posters import CHAPTER_TITLES  # noqa: E402

START = '<!-- overlay-posters:start (written by scripts/posters/update_site.py) -->'
END = '<!-- overlay-posters:end -->'


def mine():
    out = []
    for p in sorted((HERE / 'specs').glob('p[0-9][0-9]_*.py')):
        meta = importlib.import_module(p.stem).META
        if meta.get('home', 'sims') == 'sims':
            out.append((int(p.stem[1:3]), meta))
    return out


def update_nav(posters):
    path = ROOT / 'mkdocs.yml'
    lines = path.read_text().split('\n')
    start = next(i for i, l in enumerate(lines) if l.startswith('  - Posters:'))
    end = start + 1
    while end < len(lines) and (lines[end].startswith('      ') or not lines[end].strip()):
        end += 1
    while not lines[end - 1].strip():
        end -= 1
    section = '\n'.join(lines[start:end])
    add = []
    for _, meta in posters:
        target = 'sims/%s/index.md' % meta['slug']
        if target not in section:
            add.append('      - "%s": %s' % (meta['title'].replace('"', '\\"'), target))
    if add:
        lines[end:end] = add
        path.write_text('\n'.join(lines))
    return len(add)


def card(meta):
    s = meta['slug']
    t = html.escape(meta['title'])
    return ('  <a href="../sims/%s/" title="%s" style="display:block;border:1px solid #e3e7ec;border-radius:8px;overflow:hidden;text-decoration:none;color:inherit;'
            'box-shadow:0 1px 3px rgba(0,0,0,0.08);"><img src="../sims/%s/%s.png" alt="%s" loading="lazy" style="width:100%%;aspect-ratio:16/10;object-fit:cover;'
            'background:#f5f7fa;display:block;border-bottom:1px solid #eee;"><span style="display:block;padding:9px 11px;font-size:0.85rem;font-weight:600;line-height:1.3;">%s</span></a>'
            % (s, t, s, s, t, t))


def gallery(posters):
    groups = {}
    for n, meta in posters:
        groups.setdefault(meta['chapter'], []).append(meta)
    parts = [START, '', '## OER Evaluator Overlay Posters', '',
             'Thirty reference posters, one or more for each stage of the book. Each is an interactive MicroSim: explore it by hovering or pressing, then take the quiz. '
             'The ideas behind them are on the [Poster Ideas](poster-ideas.md) page.', '']
    for chapter in ['all'] + sorted(k for k in groups if k != 'all'):
        if chapter not in groups:
            continue
        head = 'Whole book' if chapter == 'all' else CHAPTER_TITLES[chapter]
        parts += ['### %s' % head, '',
                  '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:18px;margin:1em 0 1.5em;">']
        parts += [card(m) for m in groups[chapter]]
        parts += ['</div>', '']
    parts.append(END)
    return '\n'.join(parts)


def update_index(posters):
    path = ROOT / 'docs' / 'posters' / 'index.md'
    text = path.read_text()
    block = gallery(posters)
    if START in text and END in text:
        text = re.sub(re.escape(START) + '.*?' + re.escape(END), lambda m: block, text, flags=re.S)
    else:
        text = text.rstrip('\n') + '\n\n' + block + '\n'
    path.write_text(text)


if __name__ == '__main__':
    posters = mine()
    print('nav entries added:', update_nav(posters))
    update_index(posters)
    print('gallery written for %d posters' % len(posters))
