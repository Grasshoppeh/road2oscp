Nmap

After finding the box we can gather information

```
┌──(root💀hoppeh-k)-[~]
└─# nmap -T4 -p- -A 10.148.1.5
Starting Nmap 7.91 ( https://nmap.org ) at 2021-06-21 11:40 EDT
Nmap scan report for 10.148.1.5
Host is up (0.00020s latency).
Not shown: 65529 closed ports
PORT      STATE SERVICE     VERSION
22/tcp    open  ssh         OpenSSH 2.9p2 (protocol 1.99)
| ssh-hostkey: 
|   1024 b8:74:6c:db:fd:8b:e6:66:e9:2a:2b:df:5e:6f:64:86 (RSA1)
|   1024 8f:8e:5b:81:ed:21:ab:c1:80:e1:57:a3:3c:85:c4:71 (DSA)
|_  1024 ed:4e:a9:4a:06:14:ff:15:14:ce:da:3a:80:db:e2:81 (RSA)
|_sshv1: Server supports SSHv1
80/tcp    open  http        Apache httpd 1.3.20 ((Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b)
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/1.3.20 (Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b
|_http-title: Test Page for the Apache Web Server on Red Hat Linux
111/tcp   open  rpcbind     2 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2            111/tcp   rpcbind
|   100000  2            111/udp   rpcbind
|   100024  1          32768/tcp   status
|_  100024  1          32768/udp   status
139/tcp   open  netbios-ssn Samba smbd (workgroup: SMYGROUP)
443/tcp   open  ssl/https   Apache/1.3.20 (Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b
|_http-server-header: Apache/1.3.20 (Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b
|_http-title: 400 Bad Request
| ssl-cert: Subject: commonName=localhost.localdomain/organizationName=SomeOrganization/stateOrProvinceName=SomeState/countryName=--
| Not valid before: 2009-09-26T09:32:06
|_Not valid after:  2010-09-26T09:32:06
|_ssl-date: 2021-06-21T15:41:46+00:00; 0s from scanner time.
| sslv2: 
|   SSLv2 supported
|   ciphers: 
|     SSL2_RC4_128_WITH_MD5
|     SSL2_RC4_64_WITH_MD5
|     SSL2_RC4_128_EXPORT40_WITH_MD5
|     SSL2_DES_192_EDE3_CBC_WITH_MD5
|     SSL2_RC2_128_CBC_EXPORT40_WITH_MD5
|     SSL2_RC2_128_CBC_WITH_MD5
|_    SSL2_DES_64_CBC_WITH_MD5
32768/tcp open  status      1 (RPC #100024)
MAC Address: 08:00:27:69:F7:EE (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 2.4.X
OS CPE: cpe:/o:linux:linux_kernel:2.4
OS details: Linux 2.4.9 - 2.4.18 (likely embedded)
Network Distance: 1 hop

Host script results:
|_nbstat: NetBIOS name: KIOPTRIX, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
|_smb2-time: Protocol negotiation failed (SMB2)

TRACEROUTE
HOP RTT     ADDRESS
1   0.20 ms 10.148.1.5

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 59.55 seconds

```

# Analysis

As part of the class I'm taking they want us to analyze the file from the given information on our own before moving on.

**Port 22 (SSH**

- SSH Version 2.9p2 (protocol 1.99) (Version or protocol may have different exploits look at them individually?)
- Public Keys (maybe crackable, I know what I don't know and I'm making a guess here)

```
1024 b8:74:6c:db:fd:8b:e6:66:e9:2a:2b:df:5e:6f:64:86 (RSA1)
1024 8f:8e:5b:81:ed:21:ab:c1:80:e1:57:a3:3c:85:c4:71 (DSA)
1024 ed:4e:a9:4a:06:14:ff:15:14:ce:da:3a:80:db:e2:81 (RSA)
```

- Server supports SSHv1, maybe this can be abused?

**Port 80** (Apache) (I don't know a lot about this, need to research)

- Apache version httpd 1.3.20 (Check this version, may have an exploit
- mod_ssl/2.8.4 OpenSSL/0.9.6b (Check the version, may be vulnerable)
- `Potentially risky methods: TRACE`, I don't know what this means, sounds intresting though. Google it

**Port 111** rpcbind

- Not too sure what this port does, need to research
- Not sure about `rpcbind 2 (RPC #100000)` at this time, need to research
- sweet, thanks for telling me about another open port

```
|   100000  2            111/tcp   rpcbind
|   100000  2            111/udp   rpcbind
|   100024  1          32768/tcp   status
|_  100024  1          32768/udp   status
```

**port 139** (samba)

- Samba is a file mounting service, `netbios-ssn Samba smbd (workgroup: SMYGROUP)`, not sure how I can abuse ths info yet, but ti give my the group name of the share.

**port 443** (https)

- I'm not sure, but this seems out of place??? `http-title: 400 Bad Request`. Even as a regular IT a request like nmap should generally not give back an error. Worth investigating.
- "Don't worry, we will contact you, we know where you live." -Some government spy agency `ssl-cert: Subject: commonName=localhost.localdomain/organizationName=SomeOrganization/stateOrProvinceName=SomeState/countryName=--`
- Certificate is expired, if I was on your IT team I would be unhappy right now. Can this be abused, malicous cert or getting inbetween? >:(

```
Not valid before: 2009-09-26T09:32:06
Not valid after:  2010-09-26T09:32:06
```

- Not sure I don't know what I can use this for or how to act on it, need to know more.

```
| sslv2: 
|   SSLv2 supported
|   ciphers: 
|     SSL2_RC4_128_WITH_MD5
|     SSL2_RC4_64_WITH_MD5
|     SSL2_RC4_128_EXPORT40_WITH_MD5
|     SSL2_DES_192_EDE3_CBC_WITH_MD5
|     SSL2_RC2_128_CBC_EXPORT40_WITH_MD5
|     SSL2_RC2_128_CBC_WITH_MD5
|_    SSL2_DES_64_CBC_WITH_MD5
```

**Port 32768**

- something is on this port and it is related to port 111 I think, good possibility this is an entry point `32768/tcp open status 1 (RPC #100024)`

**General inferances from given info**

- **OS:** Probably Redhat / CentOS
- **OS Version**: 2.4.X (2.4.9 - 2.4.18) with high certainty
    - If the software is old and we did not pass through a IDS they probably did not see us because of a Syn, Syn-ack, Rst
- SMB running, `smb2-time: Protocol negotiation failed (SMB2)`

**Related too:**
[10.148.1.5](../../../../road_to_oscp_notes/boxes/1.kioptrix_lvl1/10.148.1.5.md)