# 🌐 Shodan Dorks

| Use Case | Shodan Query | Description |
|----------|--------------|-------------|
| Elasticsearch | `product:"Elasticsearch"` | Often exposed without auth |
| Open RDP | `port:3389` | RDP service exposure |

## 🌐 Shodan Search Filters

| Description | Query |
|-------------|-------|
| Apache OFBiz | `http.html:"Apache OFBiz"` |
| Autonomous System Number (ASN) | `asn:ASxxxx` |
| Atlassian Confluence | `http.component:"Atlassian Confluence"` |
| Atlassian Jira | `http.component:"Atlassian Jira"` |
| Atlassian Connect JSON | `html:"atlassian-connect.json"` |
| BitBucket Components | `http.component:"BitBucket"` |
| BitBucket Login Page | `title:"Log in - Bitbucket"` |
| BMC Remedy | `http.html:"BMC Remedy"` |
| Cobalt Strike Team Server | `product:"cobalt strike team server"` |
| Cobalt Strike Beacon | `product:"Cobalt Strike Beacon"` |
| Same CN on SSL certs | `ssl.cert.subject.cn:"oracle.com"` |
| Cisco Smart Install | `"smart install client active"` |
| Citrix Gateway Title | `title:"citrix gateway"` |
| Citrix Gateway HTML | `html:"/citrix/xenapp"` |
| GlobalProtect Portal | `http.html:"Global Protect"` |
| Organisation (e.g. Microsoft) | `org:microsoft` |
| Juniper Web Device Login | `http.title:"Log In - Juniper Web Device Manager"` |
| Pulse Secure VPN | `product:"Pulse Secure"` |
| Bomgar Remote Support | `"Server: Bomgar" "200 OK"` |
| MOVEit SSH Banner | `"SSH-2.0-MOVEit"` |
| SAP NetWeaver Portal | `html:"SAP NetWeaver"` |
| Unencrypted Services | `not ssl` |
| Windows RDP Fingerprint | `"\x03\x00\x00\x0b\x06\xd0\x00\x00\x124\x00"` |
