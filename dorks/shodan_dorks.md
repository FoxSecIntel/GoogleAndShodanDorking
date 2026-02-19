# 🌐 Shodan Dorks

## 🤖 AI & Agentic Systems

| Use Case | Shodan Query | Description |
| :--- | :--- | :--- |
| OpenClaw Control | `http.title:"OpenClaw Control"` | Finds OpenClaw personal AI gateway instances |
| OpenClaw (Favicon) | `http.favicon.hash:-800551065` | Fingerprint for OpenClaw/Moltbot nodes |
| Ollama API | `port:11434 "Ollama is running"` | Finds exposed Ollama LLM servers |
| Flowise AI | `http.title:"Flowise"` | Detects exposed Flowise UI instances |
| ChromaDB | `port:8000 "ChromaDB"` | Finds exposed Vector DB nodes |
| vLLM Serving | `port:8000 "vllm"` | Detects vLLM inference servers |
| Jupyter Notebook | `http.title:"Jupyter Notebook"` | Can expose notebooks, code, and tokens |
| n8n Automation | `http.favicon.hash:-831756631` | Detects exposed n8n instances |

## 🧰 Everything Else

| Use Case | Shodan Query | Description |
| :--- | :--- | :--- |
| Apache OFBiz | `http.html:"Apache OFBiz"` | Detects exposed Apache OFBiz portals |
| ASN Lookup | `asn:ASxxxx` | Finds all IPs belonging to a specific ASN |
| Atlassian Confluence | `http.component:"Atlassian Confluence"` | Finds exposed Confluence instances |
| Atlassian Jira | `http.component:"Atlassian Jira"` | Finds exposed Jira instances |
| Bitbucket Login | `title:"Log in - Bitbucket"` | Detects Bitbucket login portals |
| BMC Remedy | `http.html:"BMC Remedy"` | Detects exposed BMC Remedy portals |
| Bomgar Remote Support | `"Server: Bomgar" "200 OK"` | Detects exposed Bomgar infrastructure |
| Cisco Smart Install | `"smart install client active"` | Detects legacy Cisco Smart Install exposure |
| Citrix Gateway | `title:"citrix gateway"` | Detects Citrix login portals |
| Cobalt Strike Beacon | `product:"Cobalt Strike Beacon"` | Flags possible active beacons |
| Docker API | `port:2375 "Containers:"` | Exposed Docker remote API (high risk) |
| Elasticsearch | `product:"Elasticsearch"` | Finds often unauthenticated clusters |
| Exposed Git | `http.html:"/.git/"` | Detects publicly exposed git directories |
| Jenkins Dashboard | `http.component:"Jenkins" "Dashboard [Jenkins]"` | Finds exposed CI/CD systems |
| JupyterHub | `http.title:"JupyterHub"` | Detects exposed multi-user notebook hubs |
| MOVEit SSH Banner | `"SSH-2.0-MOVEit"` | Finds MOVEit transfer SSH exposure |
| Open RDP | `port:3389` | RDP exposure check |
| Org Asset Sweep | `org:"Microsoft"` | Finds assets attributed to an org |
| Pulse Secure VPN | `product:"Pulse Secure"` | Finds Pulse Secure endpoints |
| Redis (No Auth) | `product:Redis port:6379` | Finds potentially exposed Redis servers |
| SAP NetWeaver | `html:"SAP NetWeaver"` | Detects exposed SAP systems |
| SSL CN Pivot | `ssl.cert.subject.cn:"oracle.com"` | Pivot via shared SSL common name |

---

## 📢 Disclaimer

For educational and authorized security testing only. Always obtain explicit permission before use.
