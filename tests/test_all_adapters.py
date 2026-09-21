import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from adapters.openai_adapter import OpenAIAdapter
from adapters.crewai_adapter import CrewAIAdapter
from adapters.claude_adapter import ClaudeAdapter
from adapters.lyzr_adapter import LyzrAdapter

adapters=[OpenAIAdapter(),CrewAIAdapter(),ClaudeAdapter(),LyzrAdapter()]
ok=True
print("TestMedic Adapter Verification")
print("==============================")
for adapter in adapters:
    r=adapter.verify("tests/broken_project")
    status="PASS" if r["verified"] else "FAIL"
    ok=ok and r["verified"]
    print(f"{adapter.framework}: {status}")
    print(f"  Diagnosis: {r['result']['diagnosis']['status']}")
print()
print("All adapter verification checks: PASS" if ok else "Adapter verification checks: FAIL")
if not ok: raise SystemExit(1)
