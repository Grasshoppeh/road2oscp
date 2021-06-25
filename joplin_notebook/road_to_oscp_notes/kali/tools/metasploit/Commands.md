Commands

# starting metasploit
`msfconsole`
Exploits: self explanitory
Auxiliary: Scanning and Enumeration
Post: post exploitation
Payloads: 
encoders: 
nops: 
evasion: 

## searching

Search for a particular exploit, aux, post, payload, encoder, nops, or evasion
```
search <thing>
search smb

Results:
<thing>/<how it does the thing>/
auxiliary/gathering
auxiliary/fuzzers
exploit/windows/
```

## Using a module

**To activate a module**
```
use # (after a search)
user /path/to/thing

use 8
use auxiliary/scanner/smb/smb_version

```

**Print out info about a module**

```
info
```

**print out options about a module**

```
options
```
**Set options**
```
set <thing> <options>
```