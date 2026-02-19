# 📄 Google Dorks (SOC Use)

Collection of Google dorks organized by use case.

---

## 🤖 AI & LLM Infrastructure

| Filter | Description | Example |
| :--- | :--- | :--- |
| `intitle` | Exposed OpenClaw / Moltbot dashboards | `intitle:"OpenClaw Control" -github.com` |
| `inurl` | Exposed Ollama API instances | `inurl:11434 "Ollama is running"` |
| `intitle` | Flowise AI dashboards | `intitle:"Flowise" inurl:8080` |
| `intext` | Exposed OpenAI keys in env files | `filetype:env "OPENAI_API_KEY=sk-"` |
| `filetype` | Exposed HuggingFace tokens in logs | `filetype:log "hf_" "HuggingFace"` |
| `inurl` | Exposed ChromaDB/vector DB | `inurl:8000 "ChromaDB"` |
| `intitle` | Jupyter notebooks with AI scripts | `intitle:"Jupyter Notebook" "import openai"` |
| `site` | Public LangSmith traces | `site:smith.langchain.com/public/` |
| `intext` | Exposed Weights & Biases projects | `intext:"Weights & Biases" "Project"` |

---

## 🌍 Search Filters — `site`

| Filter | Description | Example |
|--------|-------------|---------|
| `site` | Identify subdomains excluding `www` | `site:google.com -site:www.google.com` |
| `site` | Find key people on LinkedIn by company | `site:linkedin.com bbc chief` |
| `site` | Search social footprint on X/Twitter | `site:twitter.com bbc` |
| `site` | Search S3 buckets for confidential data | `site:s3.amazonaws.com confidential companyname` |
| `site` | Search public OneDrive documents | `site:onedrive.live.com` |
| `site` | Search government data pages | `site:gov inurl:data` |
| `site` | Search admin pages on a target site | `site:example.com inurl:admin` |
| `site` | Email exposure check in paste sites | `site:pastebin.com "yourcompany.com" OR "@yourcompany.com"` |

---

## 📄 Search Filters — `intitle`

| Filter | Description | Example |
|--------|-------------|---------|
| `intitle` + `inurl` | Find open FTP-style listings | `intitle:"index of" inurl:ftp` |
| `intitle` | WordPress admin/login exposure | `intitle:"Index of" wp-admin` |
| `intitle` | Default Apache pages | `intitle:"Apache2 Ubuntu Default Page: It works"` |
| `intitle` | IIS default pages | `intitle:"IIS Windows Server" inurl:example.com` |

---

## 🔗 Search Filters — `inurl`

| Filter | Description | Example |
|--------|-------------|---------|
| `inurl` | F5 BigIP login | `inurl:/tmui/login.jsp` |
| `inurl` | Pages with "login" in URL | `inurl:login` |
| `inurl` | Services on port 8443 | `inurl:8443 -intext:8443` |

---

## 🧾 Search Filters — `intext`

| Filter | Description | Example |
|--------|-------------|---------|
| `intext` | Open directories | `intext:"index of" "parent directory"` |
| `intext` | Password mentions in pages/files | `intext:password` |

---

## 🧰 Other Operators

| Filter | Description | Example |
|--------|-------------|---------|
| `filetype` | Search for exposed private keys | `filetype:key "PRIVATE KEY-----"` |
| `intext` | Email domain match | `intext:"@domainname.com"` |
| `related` | Find related pages to a URL | `related:www.bbc.co.uk` |
| `filetype` + `inurl` | Find XLS files with email names | `filetype:xls inurl:"email.xls"` |
| `map` | Force Google Maps context | `map:london` |
| `stock` | Stock-related info | `stock:goog` |
| wildcard | Wildcard match pattern example | `fred.smith*.com` |
| `ip` | IP-based search | `ip:8.8.8.8` |

---

## 📢 Disclaimer

This cheatsheet is for educational and authorized security testing only.
Always get proper permission before using these queries in real-world environments.
