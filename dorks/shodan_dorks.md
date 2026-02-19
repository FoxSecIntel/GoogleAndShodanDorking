# 🌐 Shodan Dorks (Analyst Edition)

Designed for real SOC workflows: clear priorities, fast pivots, and practical triage value.

---

## 🤖 AI & Agentic Systems

| Priority | Use Case | Shodan Query | Why it matters | Risk | ATT&CK |
| :---: | :--- | :--- | :--- | :---: | :--- |
| P1 | OpenClaw Control exposure | `http.title:"OpenClaw Control"` | Finds exposed OpenClaw personal AI gateway instances | High | T1190 |
| P1 | OpenClaw/Moltbot fingerprint | `http.favicon.hash:-800551065` | Fingerprint-based discovery even when title changes | High | T1595 |
| P1 | Ollama API exposed | `port:11434 "Ollama is running"` | Indicates exposed local LLM runtime/API | High | T1595 |
| P2 | Flowise dashboard exposed | `http.title:"Flowise"` | Finds exposed flow-builder interfaces with creds/secrets risk | Medium | T1190 |
| P2 | ChromaDB exposure | `port:8000 "ChromaDB"` | Potential leakage of RAG/vector memory | High | T1213 |
| P2 | vLLM serving node | `port:8000 "vllm"` | Exposed inference endpoints may leak prompts/data | Medium | T1595 |
| P2 | Jupyter Notebook exposed | `http.title:"Jupyter Notebook"` | Common source of credentials, code, and tokens | High | T1552 |
| P2 | n8n automation exposure | `http.favicon.hash:-831756631` | Exposed workflow engines can enable lateral automation abuse | High | T1190 |

---

## 🚪 Initial Access & Exposed Admin Surfaces

| Priority | Use Case | Shodan Query | Why it matters | Risk | ATT&CK |
| :---: | :--- | :--- | :--- | :---: | :--- |
| P1 | Exposed Docker API | `port:2375 "Containers:"` | Direct remote container control if unauthenticated | Critical | T1611 |
| P1 | Citrix login portals | `title:"citrix gateway"` | Common edge target for credential attacks | High | T1078 |
| P1 | Pulse Secure VPN | `product:"Pulse Secure"` | Internet-facing VPN footprint for auth hardening | High | T1133 |
| P1 | Open RDP surface | `port:3389` | Broad attack surface for brute force/password spray | High | T1133 |
| P2 | Juniper web login | `http.title:"Log In - Juniper Web Device Manager"` | Exposed network device admin interface | High | T1190 |
| P2 | GlobalProtect portal | `http.html:"Global Protect"` | External VPN portal exposure mapping | Medium | T1133 |
| P2 | SAP NetWeaver portals | `html:"SAP NetWeaver"` | High-value enterprise platform exposure | High | T1190 |
| P2 | BMC Remedy interfaces | `http.html:"BMC Remedy"` | ITSM exposure can leak internal workflows | Medium | T1213 |

---

## 🏗️ CI/CD, DevOps & Code Exposure

| Priority | Use Case | Shodan Query | Why it matters | Risk | ATT&CK |
| :---: | :--- | :--- | :--- | :---: | :--- |
| P1 | Jenkins dashboards | `http.component:"Jenkins" "Dashboard [Jenkins]"` | CI/CD compromise can cascade to production | High | T1190 |
| P1 | Exposed `.git` dirs | `http.html:"/.git/"` | Source code/config/secrets disclosure | High | T1552 |
| P2 | Bitbucket login pages | `title:"Log in - Bitbucket"` | Identifies externally reachable SCM portals | Medium | T1078 |
| P2 | Atlassian Confluence | `http.component:"Atlassian Confluence"` | Sensitive docs/wiki data exposure | Medium | T1213 |
| P2 | Atlassian Jira | `http.component:"Atlassian Jira"` | Ticket leakage, internal metadata exposure | Medium | T1213 |

---

## 🗄️ Data Stores & Core Services

| Priority | Use Case | Shodan Query | Why it matters | Risk | ATT&CK |
| :---: | :--- | :--- | :--- | :---: | :--- |
| P1 | Elasticsearch exposure | `product:"Elasticsearch"` | Common unauth data exposure pattern | High | T1213 |
| P1 | Redis no-auth risk | `product:Redis port:6379` | Can enable data exfil or task abuse | High | T1213 |
| P2 | Unencrypted service sweep | `not ssl` | Finds plaintext services for transport-risk review | Medium | T1040 |

---

## 🎯 Threat Infra / Offensive Tooling Signals

| Priority | Use Case | Shodan Query | Why it matters | Risk | ATT&CK |
| :---: | :--- | :--- | :--- | :---: | :--- |
| P1 | Cobalt Strike beacon | `product:"Cobalt Strike Beacon"` | Potential active C2 infrastructure | High | T1071 |
| P1 | Cobalt Strike team server | `product:"cobalt strike team server"` | C2 management server discovery | High | T1583 |
| P2 | Cisco Smart Install legacy | `"smart install client active"` | Legacy exposure still abused in scans | Medium | T1595 |
| P2 | MOVEit SSH banner | `"SSH-2.0-MOVEit"` | Exposure mapping for high-interest transfer infra | Medium | T1595 |
| P2 | Bomgar remote support | `"Server: Bomgar" "200 OK"` | Remote support stack exposure mapping | Medium | T1133 |

---

## 🔁 Pivot Recipes (Copy/Paste)

### If alert starts with an IP
1. `ip:<IP>`
2. `ssl:"<domain-if-seen>"`
3. `asn:AS<ASN_FROM_IP>`

### If alert starts with a suspicious login panel
1. `http.title:"<panel title>"`
2. `org:"<your company>" "<panel keyword>"`
3. `hostname:"<suspected domain>"`

### If alert starts with a domain
1. `hostname:"<domain>"`
2. `ssl:"<domain>"`
3. `http.favicon.hash:<hash-if-known>`

---

## 🧭 Operator Notes

- Start with **P1** queries first (highest signal).
- Validate findings against known asset inventory before escalation.
- Some queries are noisy; prefer hostname/org/asn-constrained pivots for accuracy.
- Respect rate limits and platform terms.

---

## ⚖️ Legal / Authorization

Use only for authorized security testing and defensive investigations. Do not target systems without explicit permission.
