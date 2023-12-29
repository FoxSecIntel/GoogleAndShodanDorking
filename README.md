# Mastering Shodan Dorks: A Comprehensive Cheatsheet

Shodan dorking, also referred to as Shodan querying, involves employing advanced search operators and specialized queries to unearth data that isn't readily obtainable via conventional search engines.

Here are a few instances of Shodan querying queries I employ to uncover intriguing discoveries:

## Search Filters
| Description                                        | Example                              |
| :---------------------------------------------------| :------------------------------------|
| Cisco Smart Install  |"smart install client active" ||
| Citrix Gateway  |title:"citrix gateway" ||
| Windows RDP  |"\x03\x00\x00\x0b\x06\xd0\x00\x00\x124\x00" ||
| Apache OFBiz  | "OFBiz.Visitor=" or  http.html:"Apache OFBiz" ||


# Mastering Google Dorks: A Comprehensive Cheatsheet

Google dorking, also known as Google hacking, is the practice of using advanced search operators and specialized queries to search for information that is not easily accessible through regular search engines. 

Below are some examples of Google dorking queries that I use to discover interesting new things:

## Search filters - site
| Filter          | Description                                        | Example                              |
| :-------------- |:---------------------------------------------------| :------------------------------------|
| site    | Identify subdomains that do not include www  | site:google.com -site:www.google.com |||
| site | Find those important people on linkedin by company |site:linkedin.com bbc chief|
| site | Search linkedin for people who work in a certain location | site:linkedin.com intext:location|||
|site|Find information through social media | site:twitter.com bbc|||
|site|Search s3 buckets for confidential files | site:s3.amazonaws.com confidential companyname|||
|site| Search for documents on onedrive | site:onedrive.live.com |||
|site| Search for pages on government websites containing the word "data" |site:gov inurl:data|||
|site | Search for pages containing the word "admin" on a specific website | site:example.com inurl:admin |||

## Search filters - intitle
| Filter          | Description                                        | Example                              |
| :-------------- |:---------------------------------------------------| :------------------------------------|
| intitle/inurl | Search for open FTP servers | intitle:"index of" inurl:ftp |||
|intitle | Search for WP Admin Login pages | intitle:"Index of" wp-admin |||
| intitle | Find those default Apache2 webapages | intitle:"Apache2 Ubuntu Default Page: It works"|||
| intitle | Find those default Windows webpages per url | intitle:"IIS Windows Server" inurl:example.com|||

## Search filters - inurl
| Filter          | Description                                        | Example                              |
| :-------------- |:---------------------------------------------------| :------------------------------------|
| inurl | Find F5 Big IP Login Pages  | inurl:/tmui/login.jsp |||
|inurl | This query searches for pages that contain the word "login" in the URL | inurl:login |||
|inurl | Looking for services running on port 8443 | inurl:8443 -intext:8443|||

## Search filters - intext
| Filter          | Description                                        | Example                              |
| :-------------- |:---------------------------------------------------| :------------------------------------|
| intext    | Search for open directories  | intext:"index of" "parent directory" |||
|intext | This query searches for pages that contain the word password in the text of the page | intext:password |||



## Search filters - others
| Filter          | Description                                        | Example                              |
| :-------------- |:---------------------------------------------------| :------------------------------------|
| filetype| Search for any kind of file extensions | filetype: pdf |||
|intext | This query searches for pages that contain the word password in the text of the page | intext:password |||
|intext | Search for pages containing email addresses from a specific domain | intext:"@domainname.com"|||
|related | This query searches for pages that are related to the specified URL. | related:www.bbc.co.uk|||
| | This query searches for files types .xls and the word emails in the url | filetype:xls inurl:"email.xls"|||
|map | Forces Google to provide a map of the location | map:london|||
|stock | Finds stock related information | stock:goog|||
||Finding email addresses linked to an email address | fred.smith*.com|||
|ip|Find results based on an IP address| ip:8.8.8.8|||
