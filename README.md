# 🕵️‍♂️ Google & Shodan Dorking Toolkit

A curated, SOC-ready list of Google and Shodan dorks built for Tier 1 analysts to triage, enrich, and pivot on real-world alerts and incidents.

---

## 📁 What's Inside

| Folder | Description |
|--------|-------------|
| `dorks/` | Curated lists of Google and Shodan dorks |
| `tools/` | Python scripts to search/export dork entries and run QA checks |
| `examples/` | Screenshots and real-world use cases |

---

## 🧠 Core Use Cases

- Quickly find exposed login panels
- Locate attacker infrastructure
- Investigate suspicious domains or IPs
- Identify misconfigurations or leaked documents

---

## 🚀 Get Started

Browse content:
- [Google Dorks](dorks/google_dorks.md)
- [Shodan Dorks](dorks/shodan_dorks.md)
- [Use Case Templates](dorks/use_case_templates.md)

Run dork search helper:

```bash
python3 tools/dork_runner.py --source all --search "OpenClaw"
python3 tools/dork_runner.py --source shodan --search "Docker" --output json
```

Run repository QA checks:

```bash
python3 tools/qa_check.py
```

---

## ⚡ Quick Triage Workflow

1. Identify IOC type (domain/IP/hostname/org/keyword)
2. Run low-risk pivots (Google + Shodan)
3. Validate ownership/scope before escalation
4. Capture evidence (query, timestamp, screenshot)
5. Escalate with impact + next action

---

## 🧪 Tier 1 SOC Analyst Focus

This repo is designed to answer:
> "How do I find more about this IP/domain/alert with public OSINT tooling?"

Each dork should be annotated, tested, and linked to relevant ATT&CK techniques where possible.

---

## 🔐 Legal & Safety Guardrails

- Use this toolkit only for **authorized security testing**.
- Do **not** target systems without explicit permission.
- Follow local law and platform Terms of Service.
- Treat discovered data as sensitive and report responsibly.

---

## 🛠️ Contribution

Open a PR or issue with:
- New dorks
- Use case walkthroughs
- Enrichment scripts
- QA fixes (duplicates, malformed tables, broken queries)

---

## 📄 License

MIT — use freely, contribute back.
