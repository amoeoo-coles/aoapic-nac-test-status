#!/usr/bin/env python3
"""Pre-publish security scan of every file git would publish (tracked + untracked, not ignored).

Fails (exit 1) on:
  * forbidden artefacts: Robot log.html/report.html/output.xml/xunit.xml, pabot results, console logs,
    live object dumps (live-objects.json, live-snapshot.json, raw/ class dumps), nac-data/, .env*, cookie jars, zips
  * secret patterns: private keys, GitHub/AWS/Slack/Google tokens, Bearer/Authorization headers, APIC-cookie /
    session tokens, literal password/pwd/secret/token assignments, URLs with user:pass@
  * the literal values from the nac-test .env (--env-file, default /workspace/nac-test/.env) -- values are only
    compared in memory and never printed
  usage: security_scan.py [--env-file PATH]      (run from anywhere; scans this repo)
"""
import argparse, os, pathlib, re, subprocess, sys

SITE = pathlib.Path(__file__).resolve().parent.parent
FORBIDDEN_NAME = re.compile(r"(^|/)(log\.html|report\.html|output\.xml|xunit\.xml|summary_report\.html|combined_summary\.html|"
                            r"[^/]*console[^/]*\.log|[^/]*\.log|live-objects\.json|live-snapshot\.json|\.env(\..*)?|[^/]*\.cj|cookies[^/]*|"
                            r"[^/]*\.zip|[^/]*\.pem|[^/]*\.key|id_rsa[^/]*|\.pabotsuitenames)$", re.I)
FORBIDDEN_DIR = re.compile(r"(^|/)(robot_results|pabot_results|nac-data|raw|results|robot)/", re.I)
PATTERNS = {
    "private key": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    "github token": r"\b(ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}",
    "aws key": r"\bAKIA[0-9A-Z]{16}\b",
    "slack token": r"\bxox[abprs]-[A-Za-z0-9-]{10,}",
    "google api key": r"\bAIza[0-9A-Za-z_\-]{35}\b",
    "bearer/authorization": r"(?i)\b(authorization|bearer)\b\s*[:=]\s*['\"]?[A-Za-z0-9._\-]{20,}",
    "apic cookie/token": r"(?i)(APIC-cookie|APIC-challenge|\"token\"\s*:\s*\")\s*[=:]?\s*[A-Za-z0-9+/=_\-]{20,}",
    "jwt": r"\beyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}",
    "literal password": r"(?i)[\"']?(password|passwd|pwd|secret|api[_-]?key|access[_-]?token)[\"']?\s*[:=]\s*[\"'][^\"'\s$%{}<>]{4,}[\"']",
    "env assignment": r"(?im)^\s*(ACI_PASSWORD|PASSWORD|TOKEN|SECRET)\s*=\s*\S{3,}",
    "url credentials": r"https?://[^/\s:@'\"]+:[^/\s@'\"]+@",
}


def files():
    out = subprocess.run(["git", "-C", str(SITE), "ls-files", "-co", "--exclude-standard"], capture_output=True, text=True, check=True).stdout
    return [l for l in out.splitlines() if l]


def env_values(path):
    vals = []
    try:
        for line in open(path):
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.strip().split("=", 1)
                v = v.strip().strip("'\"")
                if v and len(v) >= 4 and not v.startswith("http") and k.upper() not in ("ACI_USERNAME",):
                    vals.append((k, v))
    except FileNotFoundError:
        pass
    return vals


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--env-file", default="/workspace/nac-test/.env")
    a = ap.parse_args()
    secrets = env_values(a.env_file)
    probs, fl = [], files()
    for f in fl:
        if FORBIDDEN_NAME.search(f) or FORBIDDEN_DIR.search(f):
            probs.append((f, "forbidden artefact (raw Robot output / logs / dumps / env / archive)")); continue
        try:
            txt = (SITE / f).read_text(errors="ignore")
        except Exception:
            continue
        for name, rx in PATTERNS.items():
            for m in re.finditer(rx, txt):
                ln = txt.count("\n", 0, m.start()) + 1
                probs.append((f"{f}:{ln}", f"{name}: {m.group(0)[:12]}…"))
        for k, v in secrets:
            if v in txt:
                probs.append((f, f"contains the value of {k} from {a.env_file} (value not shown)"))
    print(f"security scan: {len(fl)} files checked, {len(secrets)} .env value(s) compared, {len(probs)} problem(s)")
    for p in probs:
        print("  FAIL", *p)
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
