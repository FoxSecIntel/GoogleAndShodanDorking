# 🌐 Shodan Dorks

| Use Case | Shodan Query | Description |
| :--- | :--- | :--- |
| **Apache OFBiz** | `http.html:"Apache OFBiz"` | Detects exposed Apache OFBiz portals |
| **ASN Lookup** | `asn:ASxxxx` | Finds all IPs belonging to a specific ASN |
| **Atlassian Confluence** | `http.component:"Atlassian Confluence"` | Uncovers Confluence instances |
| **Atlassian Connect JSON** | `html:"atlassian-connect.json"` | Finds exposed Atlassian config files |
| **Atlassian Jira** | `http.component:"Atlassian Jira"` | Uncovers Jira instances |
| **BitBucket Components** | `http.component:"BitBucket"` | Finds Bitbucket servers |
| **BitBucket Login Page** | `title:"Log in - Bitbucket"` | Detects Bitbucket login portals |
| **BMC Remedy** | `http.html:"BMC Remedy"` | Detects exposed BMC Remedy portals |
| **Bomgar Remote Support** | `"Server: Bomgar" "200 OK"` | Detects exposed Bomgar remote support |
| **Cisco Smart Install** | `"smart install client active"` | Detects legacy Cisco exposures |
| **Citrix Gateway HTML** | `html:"/citrix/xenapp"` | Matches Citrix XenApp paths |
| **Citrix Gateway Title** | `title:"citrix gateway"` | Detects Citrix login portals |
| **Cobalt Strike Beacon** | `product:"Cobalt Strike Beacon"` | Flags possible active beacons |
| **Cobalt Strike Team Server** | `product:"cobalt strike team server"` | Finds Cobalt Strike infra |
| **Docker API** | `port:2375 "Containers:"` | Finds exposed Docker Remote APIs (High Risk) |
| **Elasticsearch** | `product:"Elasticsearch"` | Often exposed without auth |
| **Exposed Git** | `http.html:"/.git/"` | Finds repositories with exposed `.git` directories |
| **GlobalProtect Portal** | `http.html:"Global Protect"` | Palo Alto VPN detection |
| **Jenkins Dashboard** | `http.component:"Jenkins" "Dashboard [Jenkins]"` | Finds exposed CI/CD pipelines |
| **Juniper Web Device Login** | `http.title:"Log In - Juniper Web Device Manager"` | Detects Juniper device login pages |
| **Jupyter Notebook** | `http.title:"Jupyter Notebook"` | Often contains cleartext scripts and credentials |
| **MOVEit SSH Banner** | `"SSH-2.0-MOVEit"` | Finds MOVEit file transfer SSH ports |
| **Next.js** | `X-Powered-By: Next.js` | Finds web apps running Next.js |
| **Open RDP** | `port:3389` | RDP service exposure |
| **Organisation Assets** | `org:"Microsoft"` | Find all assets hosted by a specific organisation |
| **Pulse Secure VPN** | `product:"Pulse Secure"` | Finds Pulse VPN endpoints |
| **Python Env Files** | `http.html:"DATABASE_URL" "SECRET_KEY"` | Finds exposed `.env` files |
| **Redis (No Auth)** | `product:Redis +port:6379` | Finds Redis servers often used as queue brokers |
| **Running n8n servers** | `http.favicon.hash:-831756631` | Detects n8n web server via favicon hash |
| **Same CN on SSL certs** | `ssl.cert.subject.cn:"oracle.com"` | SSL pivot on shared cert common name |
| **SAP NetWeaver Portal** | `html:"SAP NetWeaver"` | Detects exposed SAP systems |
| **Unencrypted Services** | `not ssl` | Finds services that don’t use TLS |
| **Windows RDP Fingerprint** | `"\x03\x00\x00\x0b\x06\xd0\x00\x00\x124\x00"` | Identifies RDP protocol exposure |

## AI & Agentic Systems
| Use Case | Shodan Query | Description |
| :--- | :--- | :--- |
| OpenClaw Control | `http.title:"OpenClaw Control"` | Finds OpenClaw personal AI gateway instances |
| OpenClaw (Favicon) | `http.favicon.hash:-800551065` | Direct fingerprint for OpenClaw/Moltbot nodes |
| Ollama API | `port:11434 "Ollama is running"` | Finds exposed Ollama local LLM servers |
| Flowise AI | `http.title:"Flowise"` | Detects Flowise UI for LLM apps |
| ChromaDB | `port:8000 "ChromaDB"` | Finds exposed Vector Databases (RAG Memory) |
| vLLM Serving | `port:8000 "vllm"` | Detects vLLM AI serving instances |
| Jupyter Notebook | `http.title:"Jupyter Notebook"` | Often cont
