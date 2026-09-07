#!/usr/bin/env python3
"""Validate synthetic claim/file and deliverable-to-price reconciliation evidence."""
import json, sys
from pathlib import Path

def validate(data):
    if not isinstance(data, dict) or data.get("fixture_label") != "FICTIONAL TEST DATA": return ["fixture_label must be FICTIONAL TEST DATA"]
    reqs, files, work = data.get("requirements"), data.get("files"), data.get("work_packages")
    errors=[]
    if not all(isinstance(x,list) for x in (reqs,files,work)): return ["requirements, files and work_packages must be lists"]
    file_ids={f.get("id") for f in files if isinstance(f,dict)}
    for r in reqs:
        if not isinstance(r,dict) or not r.get("id") or not r.get("file_ids"):
            errors.append("requirement needs id and file_ids"); continue
        for fid in r["file_ids"]:
            if fid not in file_ids: errors.append(f"requirement {r['id']} cites missing file {fid}")
    total=0
    for w in work:
        if not isinstance(w,dict) or not w.get("id") or not w.get("acceptance_owner"):
            errors.append("work package needs id and acceptance_owner"); continue
        amount=w.get("days",0)*w.get("rate",0)
        if amount != w.get("amount"): errors.append(f"work package {w['id']} amount does not equal days times rate")
        total += amount
    if data.get("financial_total") != total: errors.append("financial_total does not reconcile to work packages")
    envelopes=data.get("envelopes")
    if not isinstance(envelopes,dict) or set(envelopes)!={"technical","financial"}: errors.append("technical and financial envelopes are required")
    elif set(envelopes["technical"]) & set(envelopes["financial"]): errors.append("technical and financial envelopes overlap")
    return errors

if __name__ == "__main__":
    try: failures=validate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
    except (IndexError,OSError,UnicodeError,json.JSONDecodeError) as exc: print(f"FAIL: {exc}"); raise SystemExit(1)
    print("PASS" if not failures else "FAIL")
    for failure in failures: print(f"[ERROR] {failure}")
    raise SystemExit(0 if not failures else 1)
