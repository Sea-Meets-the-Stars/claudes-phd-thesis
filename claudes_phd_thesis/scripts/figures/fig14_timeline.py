"""Fig 14 — timeline to completion.

What has landed and what is outstanding between the qualifying exam and the
dissertation, with the dates settled in the Q&A (rounds 1–4 of
``claude_prompts/qual_exam_prompts.md``): exam evidence freeze 2026-09-19 18:00,
exam 2026-09-21, dissertation evidence freeze 2026-09-30, submission 2026-10-02.
Bars are the working windows the prompts imply; every item is labelled with the
prompt that produces it.  Dates are typed here, not computed — the source of
each is the comment beside it.
"""

from __future__ import annotations

import datetime as dt

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

import _style as st

CAPTION = ('Everything the exam report cites exists by the 19 September freeze; the '
           'dissertation adds PAB 2.0, LS2 and the synthetic-Adg test in the eleven '
           'days after the exam, and the last of those is the first to be cut if time runs out.')

D = lambda s: dt.date.fromisoformat(s)  # noqa: E731

#: (label, start, end, state) — state: done / running / planned / optional
ITEMS = [
    ('RT-A sweep (L23 + PANGAEA), 5 rungs', '2026-09-10', '2026-09-16', 'done'),        # rt_tests.md task 12
    ('RT-B sweep (PACE-100) + PAB consistency', '2026-09-17', '2026-09-18', 'done'),   # task 13, prompt 7
    ('RT-ladder pages (IOPtics task 14)', '2026-09-18', '2026-09-18', 'done'),          # prompt 6
    ('corrected PANGAEA page, runs tree, manifest', '2026-09-18', '2026-09-18', 'done'),  # prompt 8
    ('figure set (this figure)', '2026-09-18', '2026-09-19', 'done'),                   # prompt 9
    ('qualifying-exam report (< 20 pages)', '2026-09-19', '2026-09-20', 'planned'),     # prompt 10
    ('oral (40 slides)', '2026-09-20', '2026-09-21', 'planned'),                        # prompt 11
    ('PAB 2.0: backfill, gate, full fit, site', '2026-09-22', '2026-09-30', 'planned'),  # prompt 12
    ('LS2 ladder on L23', '2026-09-22', '2026-09-28', 'planned'),                        # prompt 13
    ('synthetic-Adg aliasing experiment (cut first)', '2026-09-25', '2026-09-29', 'optional'),  # prompt 14
    ('dissertation (six chapters)', '2026-09-22', '2026-10-02', 'planned'),             # prompt 15
]
MILESTONES = [('exam evidence freeze', '2026-09-19'), ('qualifying exam', '2026-09-21'),
              ('dissertation evidence freeze', '2026-09-30'), ('submission', '2026-10-02')]
COLOR = {'done': st.CATEGORICAL[0], 'running': st.CATEGORICAL[2], 'planned': st.INK3,
         'optional': st.CATEGORICAL[3]}


def main():
    st.use_style()
    fig, ax = plt.subplots(figsize=(10, 4.6))
    for i, (label, s, e, state) in enumerate(ITEMS):
        s, e = D(s), D(e) + dt.timedelta(days=1)
        ax.barh(i, (e - s).days, left=mdates.date2num(s), height=0.6, color=COLOR[state],
                edgecolor=st.SURFACE, lw=1.2)
        ax.text(mdates.date2num(e) + 0.15, i, label, va='center', fontsize=8, color=st.INK)
    for k, (label, d) in enumerate(MILESTONES):
        x = mdates.date2num(D(d))
        ax.axvline(x, color=st.INK, lw=0.9, ls='--')
        # horizontal labels above the axes, staggered so neighbours two days apart clear
        ax.annotate(label, (x, 1.0), xycoords=('data', 'axes fraction'),
                    xytext=(0, 4 + 11 * (k % 2)), textcoords='offset points',
                    va='bottom', ha='center', fontsize=7.5, color=st.INK2)
    ax.set_yticks([])
    ax.invert_yaxis()
    ax.set_xlim(mdates.date2num(D('2026-09-09')), mdates.date2num(D('2026-10-12')))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=3))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
    ax.grid(axis='y', visible=False)
    handles = [plt.Rectangle((0, 0), 1, 1, color=COLOR[k]) for k in ('done', 'planned', 'optional')]
    ax.legend(handles, ['done', 'planned', 'optional — cut first'], loc='lower left', fontsize=8)
    fig.suptitle('Timeline to completion, 2026', fontsize=10, x=0.01, ha='left')
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    st.save(fig, 'fig14_timeline', caption=CAPTION)


if __name__ == '__main__':
    main()
