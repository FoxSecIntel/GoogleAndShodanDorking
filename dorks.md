# 🕵️ Mastering Shodan Dorks: A Comprehensive Cheatsheet

Shodan dorking (a.k.a. Shodan querying) involves using advanced search operators to discover internet-connected assets, services, and vulnerabilities that are otherwise hidden from traditional search engines.

Here are queries I use to uncover interesting data.

---

## 🌐 Shodan Search Filters

| Description | Query |
|------------|-------|
| Apache OFBiz | `http.html:"Apache OFBiz"` |
| ASN (Autonomous System Number) | `asn:ASxxxx` |
| Atlassian | `html:"atlassian-connect.json"`<br>`http.component:"Atlassian Confluence"`<br>`http.component:"Atlassian Jira"` |
| BitBucket | `http.component:"BitBucket"`<br>`title:"Log in - Bitbucket"` |
| BMC Remedy | `http.html:"BMC Remedy"` |
| CobaltStrike Servers | `product:"cobalt strike team server"`<br>`product:"Cobalt Strike Beacon"` |
| Common Name SSL match | `ssl.cert.subject.cn:"oracle.com"` |
| Cisco Smart Install | `"smart install client active"` |
| Citrix Gateway | `title:"citrix gateway"`<br>`html:"/citrix/xenapp"` |
| GlobalProtect | `http.html:"Global Protect"` |
| Organisation | `org:microsoft` |
| Juniper Router | `http.title:"Log In - Juniper Web Device Manager"` |
| Pulse Secure | `product:"Pulse Secure"` |
| Bomgar | `"Server: Bomgar" "200 OK"` |
| MoveIT | `"SSH-2.0-MOVEit"` |
| SAP | `html:"SAP NetWeaver"` |
| Cleartext | `not ssl` |
| Windows RDP | `"\x03\x00\x00\x0b\x06\xd0\x00\x00\x124\x00"` |

---

# 🔍 Mastering Google Dorks: A Comprehensive Cheatsheet

Google dorking (a.k.a. Google hacking) uses advanced search operators to extract hard-to-find information from indexed content. These queries are particularly useful for OSINT, red teaming, and recon tasks.

---

## 🌍 Search Filters – `site`

| Filter | Description | Example |
|--------|-------------|---------|
| `site` | Identify subdomains not including www | `site:google.com -site:www.google.com` |
| `site` | Find important people on LinkedIn by company | `site:linkedin.com bbc chief` |
| `site` | Find LinkedIn users by location | `site:linkedin.com intext:location` |
| `site` | Search Twitter | `site:twitter.com bbc` |
| `site` | S3 buckets for confidential data | `site:s3.amazonaws.com confidential companyname` |
| `site` | Documents on OneDrive | `site:onedrive.live.com` |
| `site` | Government data pages | `site:gov inurl:data` |
| `site` | Admin pages on a specific site | `site:example.com inurl:admin` |

---

## 📄 Search Filters – `intitle`

| Filter | Description | Example |
|--------|-------------|---------|
| `intitle` / `inurl` | Find open FTP servers | `intitle:"index of" inurl:ftp` |
| `intitle` | WordPress admin login | `intitle:"Index of" wp-admin` |
| `intitle` | Default Apache2 pages | `intitle:"Apache2 Ubuntu Default Page: It works"` |
| `intitle` | IIS default pages | `intitle:"IIS Windows Server" inurl:example.com` |

---

## 🔗 Search Filters – `inurl`

| Filter | Description | Example |
|--------|-------------|---------|
| `inurl` | F5 BigIP login | `inurl:/tmui/login.jsp` |
| `inurl` | Pages with "login" in the URL | `inurl:login` |
| `inurl` | Services on port 8443 | `inurl:8443 -intext:8443` |

---

## 🧾 Search Filters – `intext`

| Filter | Description | Example |
|--------|-------------|---------|
| `intext` | Open directories | `intext:"index of" "parent directory"` |
| `intext` | Password mentions | `intext:password` |

---

## 🧰 Search Filters – Other Operators

| Filter | Description | Example |
|--------|-------------|---------|
| `filetype` | File extension search | `filetype:pdf` |
| `intext` | Email domain match | `intext:"@domainname.com"` |
| `related` | Find related pages to a URL | `related:www.bbc.co.uk` |
| — | XLS files with "email" in URL | `filetype:xls inurl:"email.xls"` |
| `map` | Forces Google Maps location | `map:london` |
| `stock` | Stock-related info | `stock:goog` |
| — | Wildcard match on email | `fred.smith*.com` |
| `ip` | IP-based search | `ip:8.8.8.8` |

---

## 📢 Disclaimer

This cheatsheet is for **educational and authorised security testing only**. Always get proper permission before using these queries in a real-world context.

---

## 💬 Contributions

Spotted an issue or want to add more queries? Submit a Pull Request or open an Issue. Let’s keep this list evolving.

