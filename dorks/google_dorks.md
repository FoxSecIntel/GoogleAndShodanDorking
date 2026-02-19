# 📄 Google Dorks (Analyst Edition)

Designed for real SOC workflows: clear priorities, fast pivots, and practical triage value.

---

## 🤖 AI & LLM Infrastructure

| Priority | Use Case | Google Query | Why it matters | Risk | ATT&CK |
| :---: | :--- | :--- | :--- | :---: | :--- |
| P1 | Exposed OpenClaw dashboards | `intitle:"OpenClaw Control" -github.com` | Identifies potentially exposed AI control surfaces | High | T1190 |
| P1 | Exposed Ollama instances | `inurl:11434 "Ollama is running"` | Flags public LLM runtime APIs | High | T1595 |
| P2 | Flowise exposure | `intitle:"Flowise" inurl:8080` | Finds flow-builder UIs with secret/workflow risk | Medium | T1190 |
| P1 | OpenAI key leakage in env files | `filetype:env "OPENAI_API_KEY=sk-"` | Detects potential credential leakage | High | T1552 |
| P2 | HuggingFace token leakage | `filetype:log "hf_" "HuggingFace"` | Finds exposed tokens in logs/debug output | High | T1552 |
| P2 | ChromaDB exposure clues | `inurl:8000 "ChromaDB"` | Signals exposed vector DB infrastructure | Medium | T1213 |
| P2 | Jupyter notebooks with AI code | `intitle:"Jupyter Notebook" "import openai"` | Common source of cleartext secrets/scripts | High | T1552 |
| P2 | Public LangSmith traces | `site:smith.langchain.com/public/` | Can expose prompts, chains, and system behavior | Medium | T1213 |

---

## 🚪 Initial Access & Exposed Admin Surfaces

| Priority | Use Case | Google Query | Why it matters | Risk | ATT&CK |
| :---: | :--- | :--- | :--- | :---: | :--- |
| P1 | Open admin panels | `inurl:admin intitle:login` | Rapidly identifies exposed auth portals | High | T1190 |
| P1 | WordPress admin exposure | `inurl:wp-admin intitle:"login"` | Common brute-force target surface | High | T1078 |
| P1 | cPanel portals | `inurl:cpanel intitle:"cPanel"` | Finds internet-facing hosting control panels | High | T1133 |
| P2 | F5 BigIP login paths | `inurl:/tmui/login.jsp` | Detects exposed network edge login interfaces | High | T1190 |
| P2 | Citrix web access traces | `inurl:/citrix intext:"Citrix"` | Locates external Citrix access points | High | T1133 |
| P2 | Apache default pages | `intitle:"Apache2 Ubuntu Default Page: It works"` | Indicates weak hardening / exposed defaults | Medium | T1595 |
| P2 | IIS default pages | `intitle:"IIS Windows Server"` | Identifies default web server deployments | Medium | T1595 |

---

## 🏗️ CI/CD, Code & Secret Exposure

| Priority | Use Case | Google Query | Why it matters | Risk | ATT&CK |
| :---: | :--- | :--- | :--- | :---: | :--- |
| P1 | Exposed private keys | `filetype:key "PRIVATE KEY-----"` | Direct credential/private key exposure | Critical | T1552 |
| P1 | Exposed `.git` artifacts | `inurl:.git "index of"` | Source/config leakage opportunity | High | T1552 |
| P1 | Jenkins exposure clues | `intitle:"Dashboard [Jenkins]"` | CI/CD compromise can cascade to prod | High | T1190 |
| P1 | Public `.env` leaks | `filetype:env "DATABASE_URL" OR "SECRET_KEY"` | Finds direct app secret leakage | High | T1552 |
| P2 | Config backups exposed | `intitle:"index of" (".bak" OR ".old" OR "backup")` | Common accidental data exposure pattern | Medium | T1565 |
| P2 | Public Swagger/OpenAPI docs | `intitle:"Swagger UI" inurl:/swagger` | Reveals attackable API surface | Medium | T1595 |
| P2 | Kubernetes dashboard traces | `intitle:"Kubernetes Dashboard"` | Indicates potentially risky cluster exposure | High | T1190 |

---

## 🗄️ Data Exposure & Sensitive Documents

| Priority | Use Case | Google Query | Why it matters | Risk | ATT&CK |
| :---: | :--- | :--- | :--- | :---: | :--- |
| P1 | Credential dump traces | `intitle:"index of" (passwd OR credentials)` | Potential credential leak location | High | T1555 |
| P1 | Password mentions in text | `filetype:txt intext:password intext:@` | Quick sweep for leaked auth material | High | T1552 |
| P2 | Public cloud bucket docs | `site:s3.amazonaws.com confidential companyname` | Finds potentially exposed cloud objects | Medium | T1530 |
| P2 | OneDrive public docs | `site:onedrive.live.com "companyname"` | Detects accidental public file sharing | Medium | T1213 |
| P2 | Excel exports with emails | `filetype:xls inurl:email` | Possible PII/user list exposure | Medium | T1213 |
| P2 | Paste-site email exposure | `site:pastebin.com "@yourcompany.com"` | Spots leaked internal emails/IOCs | Medium | T1589 |

---

## 🎯 Threat Infra & IOC Pivoting

| Priority | Use Case | Google Query | Why it matters | Risk | ATT&CK |
| :---: | :--- | :--- | :--- | :---: | :--- |
| P1 | Pivot by suspicious IP | `"45.155.204.147"` | Finds references/reuse across open web | Medium | T1596 |
| P1 | Pivot by domain keyword | `"example.com" (malware OR phishing OR leak)` | Fast context on known suspicious domains | Medium | T1596 |
| P2 | Related-site pivot | `related:example.com` | Expands discovery around known infrastructure | Low | T1595 |
| P2 | Subdomain discovery | `site:example.com -www` | Identifies potential unmanaged hosts | Medium | T1595 |
| P2 | ASN/Org clueing via docs | `"AS12345" "example.com"` | Correlates org/infra breadcrumbs in public docs | Low | T1596 |

---

## 🔁 Pivot Recipes (Copy/Paste)

### If alert starts with an IP
1. `"<IP>" site:pastebin.com OR site:github.com`
2. `"<IP>" "C2" OR "phishing"`
3. `"<IP>" "index of"`

### If alert starts with a suspicious domain
1. `site:<domain> -www`
2. `"<domain>" (phishing OR malware OR credential)`
3. `site:pastebin.com "<domain>"`

### If alert starts with an exposed login/service
1. `inurl:login "<brand/product>"`
2. `intitle:"<product>" "admin"`
3. `"<fqdn-or-ip>" "default page"`

---

## 🧭 Operator Notes

- Start with **P1** entries first (highest signal/impact).
- Constrain searches with `site:` and explicit IOC terms to reduce noise.
- Expect false positives on generic terms (`login`, `admin`) unless combined with context.
- Capture evidence: query, timestamp, screenshot, and confidence level.

---

## ⚖️ Legal / Authorization

Use only for authorized security testing and defensive investigations. Do not target systems without explicit permission.
