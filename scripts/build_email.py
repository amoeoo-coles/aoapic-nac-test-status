#!/usr/bin/env python3
"""Build the Gmail-friendly HTML email (inline CSS, tables only) for one run + its changes.json.

  build_email.py [--run STAMP] [--out /tmp/aoapic-email-STAMP.html] [--sample]
Prints the suggested subject on stdout. The file is written OUTSIDE the repo by default so it is never published.
"""
import argparse, datetime as dt, html, json, pathlib, re

SITE = pathlib.Path(__file__).resolve().parent.parent
DATA = SITE / "data"
PAGE = "https://amoeoo-coles.github.io/aoapic-nac-test-status/"
STAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{4}$")
e = lambda s: html.escape(str(s if s is not None else ""))
TD = "padding:6px 9px;border:1px solid #e3e8f0;font-size:13px;vertical-align:top;"
TH = TD + "background:#f1f4f9;font-weight:bold;text-align:left;color:#334155;"
RED, GRN, AMB, MUT = "#c62828", "#1b7f45", "#9a6200", "#5d6b7e"


def load(p):
    try:
        return json.load(open(p))
    except Exception:
        return {}


def delta(d, bad=1):
    if not d:
        return f'<span style="color:{MUT}">&ndash;</span>'
    c = MUT if not bad else (RED if (d > 0) == (bad > 0) else GRN)
    return f'<b style="color:{c}">{d:+d}</b>'


def table(head, rows, right_from=1):
    h = "".join(f'<th style="{TH}{"text-align:right;" if i >= right_from else ""}">{x}</th>' for i, x in enumerate(head))
    b = "".join("<tr>" + "".join(f'<td style="{TD}{"text-align:right;" if i >= right_from else ""}">{x}</td>' for i, x in enumerate(r)) + "</tr>" for r in rows)
    return f'<table cellpadding="0" cellspacing="0" style="border-collapse:collapse;width:100%;max-width:760px;margin:6px 0 14px;">{h and "<tr>"+h+"</tr>"}{b}</table>'


def h2(t):
    return f'<h2 style="font-size:16px;margin:20px 0 6px;color:#0b1d33;border-bottom:2px solid #1f6feb;padding-bottom:3px;">{t}</h2>'


def pills(a, bg, fg):
    return " ".join(f'<span style="display:inline-block;background:{bg};color:{fg};border-radius:10px;padding:1px 8px;margin:1px;font-size:12px;font-weight:bold;">{e(x)}</span>' for x in a) or f'<span style="color:{MUT}">none</span>'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run"); ap.add_argument("--out"); ap.add_argument("--sample", action="store_true")
    a = ap.parse_args()
    stamp = a.run or sorted(p.name for p in DATA.iterdir() if p.is_dir() and STAMP_RE.match(p.name))[-1]
    d = DATA / stamp
    daily, drift, integ, C = (load(d / f) for f in ("daily-summary.json", "drift-summary.json", "integrity-summary.json", "changes.json"))
    r, t = integ.get("robot", {}), drift.get("tests", {})
    sc = integ.get("scorecard", [])
    nb = sum(x["status"] == "BROKEN" for x in sc)
    status = daily.get("status")
    col = RED if status in ("attention", "error") and integ.get("broken") else (AMB if status != "ok" else GRN)
    day = dt.datetime.strptime(stamp[:10], "%Y-%m-%d")
    subject = f"{'SAMPLE – ' if a.sample else ''}AOAPIC drift report – {day.strftime('%a')} {day.day} {day.strftime('%b %Y')}"
    P = []
    P.append(f'<div style="font-family:Arial,Helvetica,sans-serif;color:#16202e;max-width:780px;">')
    if a.sample:
        P.append(f'<p style="background:#fff4dc;border:1px solid #f3d38a;padding:8px 12px;font-size:13px;margin:0 0 10px;">'
                 f'<b>SAMPLE run</b> of the weekday 8 AM routine, so you can check the format. Compared with this morning&rsquo;s 11:05 AEDT run as &ldquo;previous morning&rdquo;.</p>')
    P.append(f'<table cellpadding="0" cellspacing="0" style="width:100%;max-width:760px;border-collapse:collapse;"><tr><td style="background:#0b1d33;color:#ffffff;padding:14px 16px;">'
             f'<div style="font-size:19px;font-weight:bold;">AOAPIC nac-test daily report</div>'
             f'<div style="font-size:13px;opacity:.85;">Cisco DevNet Always-On APIC sandbox · APIC snapshot {e(integ.get("pulled_at_local"))} (Melbourne, AEDT)</div></td></tr>'
             f'<tr><td style="background:{col};color:#ffffff;padding:10px 16px;font-size:15px;font-weight:bold;">{e(daily.get("headline"))}</td></tr>'
             f'<tr><td style="background:#f5f7fb;padding:10px 16px;font-size:13px;line-height:1.5;">'
             f'Integrity tests <b>{r.get("passed")}/{r.get("total")}</b> passed ({r.get("failed")} failed) · Drift tests <b>{t.get("passed")}/{t.get("total")}</b> passed ({t.get("failed")} failed)<br>'
             f'<b style="color:{RED}">{integ.get("broken")}</b> broken relations · <b style="color:{AMB}">{integ.get("warnings")}</b> warnings · <b>{nb}</b> of {len(sc)} tenants broken<br>'
             f'<a href="{PAGE}" style="color:#1f6feb;font-weight:bold;">Open the live status page &rarr;</a></td></tr></table>')
    if C.get("previous"):
        T, tn, br, fl = C["tests"], C["tenants"], C["broken_relations"], C["faults"]
        P.append(h2(f"Changes since previous morning ({e(C['previous_snapshot'])})"))
        rows = [("Integrity tests", T["integrity"]["total"], 0), ("Integrity passed", T["integrity"]["passed"], -1),
                ("Integrity failed", T["integrity"]["failed"], 1), ("Drift tests", T["drift"]["total"], 0),
                ("Drift passed", T["drift"]["passed"], -1), ("Drift failed", T["drift"]["failed"], 1),
                ("Broken relations", {"prev": br["prev"], "now": br["now"]}, 1), ("Warnings", C["warnings"], 1),
                ("Tenants on APIC", {"prev": tn["prev_total"], "now": tn["now_total"]}, 0),
                ("Tenants broken", {"prev": tn["broken_prev"], "now": tn["broken_now"]}, 1),
                ("Critical faults (fabric)", fl["fabric_totals"]["critical"], 1), ("Major faults (fabric)", fl["fabric_totals"]["major"], 1)]
        P.append(table(["Metric", "Prev morning", "Now", "&Delta;"],
                       [(e(l), v["prev"], f"<b>{v['now']}</b>", delta(v["now"] - v["prev"], b)) for l, v, b in rows]))
        P.append(h2("Tenant changes"))
        P.append(table([], [(f'<b style="color:{RED}">Newly broken</b>', pills(tn["newly_broken"] + [x + " (new)" for x in tn["added_broken"]], "#fde8e8", RED)),
                            (f'<b style="color:{GRN}">Fixed</b>', pills(tn["fixed"], "#e5f6ed", GRN)),
                            ('<b style="color:#1a56c4">Added</b>', pills(tn["added"], "#e8f0fe", "#1a56c4")),
                            (f'<b style="color:{MUT}">Removed</b>', pills(tn["removed"], "#eef2f8", "#475569"))], right_from=9))
        sc_ch = [x for x in tn.get("status_changes", []) if x["prev"] != x["now"]]
        if sc_ch:
            P.append(table(["Tenant", "Prev", "Now", "Score"], [(e(x["tenant"]), e(x["prev"]), f"<b>{e(x['now'])}</b>", f"{x['prev_score']} &rarr; {x['now_score']}") for x in sc_ch], right_from=3))
        P.append(h2(f"Broken relations: +{len(br['added'])} added / &minus;{len(br['resolved'])} resolved"))
        brr = [("ADDED", RED, x) for x in br["added"]] + [("RESOLVED", GRN, x) for x in br["resolved"]] + \
              [("REASON CHANGED", MUT, x) for x in br.get("reason_changed", [])]
        P.append(table(["Change", "Tenant", "Check", "Object / why"],
                       [(f'<b style="color:{c}">{k}</b>', f"<b>{e(x['tenant'])}</b>", e(x["check"]),
                         f'<span style="font-family:Consolas,monospace;font-size:12px;">{e(x["dn"])}</span><br><span style="color:{MUT};font-size:12px;">{e(x["reason"])}</span>')
                        for k, c, x in brr] or [("none", "", "", "")], right_from=9))
        P.append(h2(f"New critical faults ({len(fl['new_critical'])})"))
        P.append(table(["Code", "Tenant", "Affected / description"],
                       [(f"<b>{e(f['code'])}</b>", e(f["tenant"]), f'<span style="font-family:Consolas,monospace;font-size:12px;">{e(f["affected"])}</span><br><span style="color:{MUT};font-size:12px;">{e(f["descr"])}</span>')
                        for f in fl["new_critical"]] or [("none", "", "")], right_from=9))
        if fl.get("new_major"):
            P.append(f'<p style="font-size:13px;">Also {len(fl["new_major"])} new major fault(s): ' + ", ".join(e(f"{f['code']} {f['tenant']}") for f in fl["new_major"]) + "</p>")
        P.append(h2("Drift vs baseline (object counts)"))
        P.append(table(["Type", "Baseline", "Prev morning", "Now", "&Delta;", "+ vs base", "&minus; vs base"],
                       [(e(x["type"]), x["baseline"], x["prev"], f"<b>{x['now']}</b>", delta(x["delta"], 0) if x["delta"] else delta(0), x["added_vs_baseline"], x["removed_vs_baseline"]) for x in C["drift_table"]]))
        do = C.get("drift_objects", {})
        if do.get("newly_removed_from_baseline"):
            P.append(f'<p style="font-size:13px;"><b style="color:{RED}">Baseline objects deleted since previous morning:</b> ' +
                     ", ".join(f'<span style="font-family:Consolas,monospace;font-size:12px;">{e(x["dn"])}</span>' for x in do["newly_removed_from_baseline"]) + "</p>")
    else:
        P.append("<p>No previous morning run to compare with yet.</p>")
    P.append(f'<p style="font-size:12px;color:{MUT};margin-top:18px;">Read-only checks (aaaLogin + GETs only; nothing is pushed to the APIC). The DevNet sandbox is shared, so most changes are other users&rsquo; lab objects. '
             f'Live page: <a href="{PAGE}" style="color:#1f6feb;">{PAGE}</a> · run data: <a href="{PAGE}data/{stamp}/" style="color:#1f6feb;">data/{stamp}/</a></p></div>')
    out = pathlib.Path(a.out or f"/tmp/aoapic-email-{stamp}.html")
    out.write_text("".join(P))
    print(subject); print(out)


if __name__ == "__main__":
    main()
