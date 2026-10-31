"""Regenerates the PNG figures from the two CSV files in this folder.
Run from the paper folder:  python3 figures/make_figures.py"""
import csv, statistics
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE, ORANGE, GREEN, VERM, PURPLE, SKY = "#0072B2", "#E69F00", "#009E73", "#D55E00", "#CC79A7", "#56B4E9"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.spines.top": False, "axes.spines.right": False})

rows = list(csv.DictReader(open("figures/public-oer-scores.csv")))
one = {r["resource"]: r for r in csv.DictReader(open("figures/public-oer-scores-onechapter.csv"))}
short = {"Eloquent JavaScript 4e": "Eloquent JS", "Think Python 3e": "Think Python", "OpenIntro Statistics 4e": "OpenIntro Stats",
         "OpenStax Calculus Vol 1": "OS Calculus 1", "OpenStax Biology 2e": "OS Biology", "OpenStax Anatomy & Physiology 2e": "OS Anat. & Phys.",
         "Beezer Linear Algebra 3.50": "Beezer Lin. Alg.", "OpenStax Psychology 2e": "OS Psychology",
         "OpenStax Principles of Economics 3e": "OS Economics", "OpenStax College Physics 2e": "OS Physics"}

# Figure 1: Q versus R (numbered markers, key at right)
order = sorted(rows, key=lambda r: -int(r["total"]))
fig, ax = plt.subplots(figsize=(6.6, 4.6))
ax.plot([20, 50], [20, 50], color="#BBBBBB", lw=0.8, zorder=1)
ax.fill_between([37.5, 50], 37.5, 50, color=GREEN, alpha=0.10)
seen = {}
for i, r in enumerate(order, 1):
    q, rr = int(r["Q"]), int(r["R"]); op = r["resource"].startswith("OpenStax")
    k = seen.get((q, rr), 0); seen[(q, rr)] = k + 1
    rr = rr + (0.5 if k else 0)   # offset points with identical (Q, R) so both stay visible
    ax.scatter(rr, q, s=190, marker="o" if op else "s", color=BLUE if op else ORANGE, edgecolor="black", linewidth=0.6, zorder=3)
    ax.text(rr, q, str(i), ha="center", va="center", fontsize=7.5, color="white", fontweight="bold", zorder=4)
ax.set_xlim(29, 44); ax.set_ylim(26, 43)
ax.set_xlabel("Reusability subtotal R (out of 50)"); ax.set_ylabel("Quality subtotal Q (out of 50)")
key = "\n".join(f"{i}  {short.get(r['resource'], r['resource'])} ({r['total']})" for i, r in enumerate(order, 1))
ax.text(1.02, 1.0, key, transform=ax.transAxes, va="top", fontsize=7.5, linespacing=1.5)
ax.text(1.02, 0.30, "Circle: OpenStax\nSquare: other publisher\nShaded: Q and R both\nat least 75% of 50", transform=ax.transAxes, va="top", fontsize=7.5, linespacing=1.5, color="#444444")
fig.tight_layout(); fig.savefig("figures/qr-scatter.png", dpi=300, bbox_inches="tight"); plt.close(fig)

# Figure 2: metric profile
names = ["Accuracy &\ncurrency", "Alignment", "Read-\nability", "Access-\nibility", "Practice &\nfeedback", "Open\nlicense", "Modularity", "Metadata", "Editable\nsource", "Portability"]
fig, ax = plt.subplots(figsize=(7.6, 3.6))
for i in range(10):
    v = [int(r["m%d" % (i + 1)]) for r in rows]
    c = BLUE if i < 5 else VERM
    ax.plot([i, i], [min(v), max(v)], color=c, lw=3, alpha=0.35, solid_capstyle="round")
    ax.scatter([i] * len(v), v, s=10, color=c, alpha=0.7, zorder=3)
    ax.scatter([i], [statistics.mean(v)], marker="D", s=38, color=c, edgecolor="black", linewidth=0.6, zorder=4)
ax.axvline(4.5, color="#999999", lw=0.8, ls="--")
ax.text(2, 0.3, "Quality metrics", ha="center", color=BLUE, fontsize=8.5); ax.text(7, 0.3, "Reusability metrics", ha="center", color=VERM, fontsize=8.5)
ax.set_xticks(range(10)); ax.set_xticklabels(names, fontsize=7); ax.set_ylim(0, 10.5); ax.set_ylabel("Score (0 to 10)")
fig.tight_layout(); fig.savefig("figures/metric-profile.png", dpi=300); plt.close(fig)

# Figure 3: census histogram
c = list(csv.DictReader(open("figures/census-book-checks.csv")))
counts = {}
for r in c: counts[int(r["checks_passed"])] = counts.get(int(r["checks_passed"]), 0) + 1
fig, ax = plt.subplots(figsize=(5.6, 3.2))
xs = list(range(0, 14)); ax.bar(xs, [counts.get(x, 0) for x in xs], color=SKY, edgecolor="black", linewidth=0.5)
ax.set_xticks(xs); ax.set_xlabel("Deterministic completeness checks passed (out of 13)"); ax.set_ylabel("Number of textbooks")
med = statistics.median(int(r["checks_passed"]) for r in c)
ax.axvline(med, color=VERM, lw=1.2, ls="--"); ax.text(med + 0.15, max(counts.values()) * 0.92, f"median {med:g}", color=VERM, fontsize=8)
fig.tight_layout(); fig.savefig("figures/census-histogram.png", dpi=300); plt.close(fig)
print("ok")

# Figure 5: one-chapter pass versus three-chapter pass, totals
fig, ax = plt.subplots(figsize=(4.6, 4.4))
ax.plot([55, 85], [55, 85], color="#BBBBBB", lw=0.8, zorder=1)
ax.axhline(75, color="#999999", lw=0.8, ls=":"); ax.axvline(75, color="#999999", lw=0.8, ls=":")
for i, r in enumerate(order, 1):
    x = int(one[r["resource"]]["total"]); y = int(r["total"]); op = r["resource"].startswith("OpenStax")
    ax.scatter(x, y, s=150, marker="o" if op else "s", color=BLUE if op else ORANGE, edgecolor="black", linewidth=0.6, zorder=3)
ax.set_xlim(55, 86); ax.set_ylim(55, 86)
ax.set_xlabel("Total, first pass (one chapter)"); ax.set_ylabel("Total, second pass (three chapters)")
ax.text(75.4, 56, "Adopt line (75)", fontsize=7, color="#555555")
fig.tight_layout(); fig.savefig("figures/passes-scatter.png", dpi=300); plt.close(fig)
