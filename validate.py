#!/usr/bin/env python3
import json, sys
from pathlib import Path
root=Path(__file__).parent
errors=[]
files=sorted(root.glob("workflows/*/workflow.json"))
for p in files:
    try: w=json.loads(p.read_text())
    except Exception as e: errors.append(f"{p}: {e}"); continue
    names=[n.get("name") for n in w.get("nodes",[])]
    if len(names)!=len(set(names)): errors.append(f"{p}: duplicate node names")
    if any(n.get("credentials") for n in w.get("nodes",[])): errors.append(f"{p}: embedded credentials")
    if not any(n.get("type")=="n8n-nodes-base.odoo" for n in w.get("nodes",[])): errors.append(f"{p}: no Odoo node")
    for source, outputs in w.get("connections",{}).items():
        if source not in names: errors.append(f"{p}: unknown source {source}")
        for group in outputs.get("main",[]):
            for edge in group or []:
                if edge.get("node") not in names: errors.append(f"{p}: unknown target {edge.get('node')}")
    text=p.read_text()
    for marker in ("password", "api_key", "access_token", "client_secret"):
        if marker in text.lower(): errors.append(f"{p}: forbidden secret-like field {marker}")
print(f"checked {len(files)} workflows")
if errors:
    print("FAIL")
    print("\n".join(errors)); sys.exit(1)
print("ALL OK: JSON valid, graphs connected, Odoo nodes present, no embedded credentials")
