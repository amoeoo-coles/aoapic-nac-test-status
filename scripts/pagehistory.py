"""(Copy of /workspace/report17/pagehistory.py for this repo; folder "." = the status page itself.)
Version history for site pages, built from the real git history of /workspace/ghio (git log on <folder>/index.html).
Each committed version of the page gets an entry (version number, Melbourne time, commit subject + page size, commit and branch)
and an archived snapshot recovered with `git show <commit>:<folder>/index.html`, saved to <folder>/versions/v<N>-<commit>/index.html.
The page as generated now is listed as the current version. Nothing is invented: versions are commits.
Usage (static pages): python3 pagehistory.py <folder> "<summary of the current version>" """
import datetime as dt, html, pathlib, re, subprocess, sys
from zoneinfo import ZoneInfo
REPO = pathlib.Path(__file__).resolve().parent.parent; GH = 'https://github.com/amoeoo-coles/aoapic-nac-test-status'
MEL = ZoneInfo('Australia/Melbourne'); E = lambda x: html.escape('' if x is None else str(x))
VH_RX = re.compile(r'<!--vh-->.*?<!--/vh-->', re.S)
GC_RX = re.compile(r'<script data-goatcounter=[^>]*>\s*</script>')

def git(*a): return subprocess.run(['git', *a], cwd=REPO, capture_output=True, text=True).stdout
def mel(iso): return dt.datetime.fromisoformat(iso).astimezone(MEL).strftime('%d %b %Y %H:%M %Z')

_FP = None
def branch_of(h):
    """'main' if the commit was made on main's first-parent line, else the branch named in the merge commit that brought it in."""
    global _FP
    if _FP is None: _FP = set(git('rev-list', '--first-parent', 'main').split())
    if h in _FP: return 'main'
    for line in git('log', '--merges', '--ancestry-path', '--reverse', '--format=%H %s', h + '..main').splitlines():
        m, s = line.split(' ', 1)
        if subprocess.run(['git', 'merge-base', '--is-ancestor', h, m + '^2'], cwd=REPO).returncode == 0:
            r = re.match(r"Merge (?:branch '([^']+)'|([^\s:]+))", s)
            return (r.group(1) or r.group(2)) if r else 'merged branch'
    return 'branch (not merged)'

def versions(folder):
    path = folder + '/index.html'; out = []
    for line in git('log', '--format=%H\x1f%cI\x1f%s', '--', path).splitlines():
        h, when, subj = line.split('\x1f')
        size = git('cat-file', '-s', h + ':' + path).strip()
        out.append({'h': h, 'short': h[:7], 'when': when, 'subj': subj, 'size': int(size) if size.isdigit() else None})
    out.reverse()
    for i, v in enumerate(out, 1): v['n'] = i
    return out

def _rel(m):
    attr, url = m.group(1), m.group(2)
    if re.match(r'^(?:[a-z][a-z0-9+.-]*:|//|/|#|\?)', url, re.I) or url == '': return m.group(0)
    return attr + '="../../' + url + '"'

def snapshot(folder, v):
    d = REPO / folder / 'versions' / ('v' + str(v['n']) + '-' + v['short']); f = d / 'index.html'
    if f.exists(): return d.name
    src = subprocess.run(['git', 'show', v['h'] + ':' + folder + '/index.html'], cwd=REPO, capture_output=True, text=True)
    if src.returncode: return None
    s = GC_RX.sub('', VH_RX.sub('', src.stdout))
    s = re.sub(r'\b(href|src)="([^"]*)"', _rel, s)
    s = s.replace('<head>', '<head><meta name="robots" content="noindex">', 1)
    ban = ('<div style="background:#302d20;border-left:4px solid #fc6;color:#eee;padding:10px 14px;margin:0 0 14px;font:14px system-ui,sans-serif">'
           '<b>Archived version v' + str(v['n']) + '</b> of /' + ('aoapic-nac-test-status' if folder == '.' else E(folder)) + '/ — commit <a style="color:#8cf" href="' + GH + '/commit/' + v['h'] + '">' + v['short'] + '</a>, '
           + E(mel(v['when'])) + ' (Melbourne time). Not live. Recovered from git; links, images and downloads open the current files. '
           '<a style="color:#8cf" href="../../">Latest version →</a></div>')
    s = re.sub(r'(<body[^>]*>)', lambda m: m.group(1) + ban, s, count=1)
    d.mkdir(parents=True, exist_ok=True); f.write_text(s)
    return d.name

def section(folder, current_summary, current_when=None, show=5):
    vs = versions(folder); cur = (current_when or dt.datetime.now(MEL)).astimezone(MEL).strftime('%d %b %Y %H:%M %Z')
    snaps = {v['n']: snapshot(folder, v) for v in vs}
    def li(v):
        b = branch_of(v['h']); sn = snaps.get(v['n'])
        return ('<li><b>v' + str(v['n']) + '</b> · ' + E(mel(v['when'])) + ' (Melbourne time) · ' + E(v['subj'][:170] + ('…' if len(v['subj']) > 170 else '')) +
                 ' <span style="color:#bbb">page ' + (str(round(v['size'] / 1024, 1)) + ' KB' if v['size'] else 'size n/a') + '</span> · commit <a href="' + GH + '/commit/' + v['h'] + '"><code>' + v['short'] + '</code></a>'
                ' on <code>' + E(b) + '</code>' + (' · <a href="versions/' + sn + '/">archived snapshot</a>' if sn else ' · snapshot not recoverable') + '</li>')
    items = ['<li><b>v' + str(len(vs) + 1) + ' (current)</b> · ' + E(cur) + ' (Melbourne time) · ' + E(current_summary) + ' · <a href="./">this page</a></li>'] + [li(v) for v in reversed(vs)]
    intro = (str(len(vs) + 1) + ' versions: ' + str(len(vs)) + ' committed versions from git history of <code>' + E(folder) + '/index.html</code> plus the current one.'
             if vs else 'Only the latest version of this page exists; there is no earlier committed version.')
    out = ('<!--vh--><section aria-label="Version history" id="version-history"><h2>Version history</h2><p>' + intro +
           ' Each entry is a real commit of this page (summary = commit message, with the page size at that commit). Archived snapshots are recovered from git and are not live.</p><ul>' + ''.join(items[:show]) + '</ul>')
    if len(items) > show: out += '<details><summary>Show all ' + str(len(items)) + ' versions</summary><ul>' + ''.join(items[show:]) + '</ul></details>'
    return out + '</section><!--/vh-->'

def apply(folder, current_summary, current_when=None, anchor=None):
    f = REPO / folder / 'index.html'; s = VH_RX.sub('', f.read_text())
    sec = section(folder, current_summary, current_when)
    if anchor and anchor in s: s = s.replace(anchor, sec + anchor, 1)
    else: s = s.replace('</h1>', '</h1>' + sec, 1) if '</h1>' in s else s.replace('</main>', sec + '</main>', 1)
    f.write_text(s); return sec.count('<li>')

if __name__ == '__main__':
    print(sys.argv[1], apply(sys.argv[1], sys.argv[2], anchor=sys.argv[3] if len(sys.argv) > 3 else None), 'entries')
