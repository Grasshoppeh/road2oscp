Subnetting

# Subnetting (the cheating way)

| Replace X | 128 | 192 | 224 | 240 | 248 | 252 | 254 | 255 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Subnet (1-8) |     |     |     | x.0.0.0 |     |     |     |     |
| CIDR | /1  | /2  | /3  | /4  | /5  | /6  | /7  | /8  |
| Hosts | 2,147,483,648 | 1,073,741,824 | 536,870,912 | 268,435,456 | 134,217,728 | 67,108,864 | 33,554,432 | 16,777,216 |
| Subnet (9-16) |     |     |     | 255.x.0.0 |     |     |     |     |
| CIDR | /9  | /10 | /11 | /12 | /13 | /14 | /15 | /16 |
| Hosts | 8,388,608 | 4,194,304 | 2,097,152 | 1,048,576 | 524,288 | 262,144 | 131,072 | 65,536 |
| Subnet (17-24) |     |     |     | 255.255.x.0 |     |     |     |     |
| CIDR | /17 | /18 | /19 | /20 | /21 | /22 | /23 | /24 |
| Hosts | 32,768 | 16,384 | 8,192 | 4,096 | 2,048 | 1024 | 512 | 256 |
| Subnet (25-32) |     |     |     | 255.255.255.x |     |     |     |     |
| CIDR | /25 | /26 | /27 | /28 | /29 | /30 | /31 | /32 |
| Hosts | 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |

1.  Find the Cider note of your network (ex that of a **/24**)
2.  Correspond that too the proper subnet (ex: Subnet (25-32) has 255.255.x.0)
3.  Replace x with the column it aligns with, /24 aligns with 255 in the top right

Gotcha: For the total number of hosts available always subtract 2, for example  256 has 254 Ip's available