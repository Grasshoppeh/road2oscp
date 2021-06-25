SSH

Older SSH Servers:
Might not be able to neg key exchange, there is a way around it.

`ssh <ip> -oKexAlgorithms=+<exchange method above> -c <cipher>`

1. try to connect with ssh for the error
```
Unable to negotiate with 10.148.1.5 port 22: no matching key exchange method found. Their offer: diffie-hellman-group-exchange-sha1,diffie-hellman-group1-sha1
```
2.  Add the keyalgo listed above along with one of the listed key exchange methods
```
Unable to negotiate with 10.148.1.5 port 22: no matching cipher found. Their offer: aes128-cbc,3des-cbc,blowfish-cbc,cast128-cbc,arcfour,aes192-cbc,aes256-cbc,rijndael128-cbc,rijndael192-cbc,rijndael256-cbc,rijndael-cbc@lysator.liu.se
```
4.  Run that and add the cipher with the c flag