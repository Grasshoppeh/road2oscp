Passive Reconnaissance

# Passive

## Physical / Social
**Locational Information:**
- Satellite images
	- Find out the layout of the premesis, planning out and memorizing where everything is
- drone recon
	- If the airspace is unrestricted and you have your drone operater license, you can legally fly a drone over their property in most place. Taking a drone out of the air is a federal crime without proper authority :)
- building layout
	- badge readers
		- Where they are, is there any holes you can get by?
	- break areas
		- smoking area, easy way to blend in with a fake cig and tailgate. Door might be propped open too.
	- security
		- Is there posted security anywhere?
		- Do they have routes or stick in one spot?
	- fencing
		- Small fence sure whatever, barbed fence,, not cool

**Job Information:**
- Employees
	- names
		- Knowing other people makes you belivable
	- job title
		- Knowning what people do can help you blend in
	- phone number
		- Phishing, gathering information, etc
	- manager
		- If you pose as someone in a department its a good idea to know who your manager is.
- Pictures
	- badge photos
		- People post these online for some reason in company photos... Probably learn a lot about people from this.
	- desk photos
		- What's on there desk?
		- Any papers, what's on them?
		- Anything that hints to information about their business
	- computer photos
		- OS their running?
		- Programs?
		- Other information

## Web / Host

**Target Validation:**
- Run WHOIS, nslookup, dnsrecon
- You need to validate your target, attacking the wrong target can put you in jail. Verify you have the correct one. **It is possible for someone to fat finger a number or address.**

**Finding Subdomains:**
- Bit of Google Fu, dig, nmap, sublist3r, bluto, crt.sh, etc
- Once you have a target find their subdomains and see what you can find from that.

**Fingerprinting:**
- nmap, wappalyzer, whatweb, builtwith, netcat
- We need to know what's running on a website, what services, what ports are they using, what version is everything?
- Passive approach here might just be visiting their website, active would be scanning it

**Data Breaches:**
- Check them on HaveIBeenPwned, Breach-Parse, WeLeakInfo
- Sometimes there is information already available on a target. Including email addresses, password, locational information, etc
- One of the most common way to get it, use these.

**In general the better info gathering you can do the better you will do. Recon is one of the most important topics.**

