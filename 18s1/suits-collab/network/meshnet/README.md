# meshnet

## Description

My server seems to have gone off the grid. Can you help me get back in?

`[fca4:abc2:7079:3165:a685:53a6:394e:ff4c]:6374`  

## Hint

that's a weird first octet in the IP address

## How to solve

1. Find out about Hyperboria. Possible paths to this:  
   * Googling `meshnet ipv6` should get you to docs.meshwith.me and hyperboria.net. Top 3 results are relevant.
   * Googling `meshnet` should get you to /r/darknetplan (result 3) and hyperboria.net (result 5).
   * Notice the unusual IPv6 address, it sits in fc00::/8. Googling `fc00` should point you the following, in order:
     * fc00.org
     * hyperboria.net
3. Install [cjdns](https://github.com/cjdelisle/cjdns) and configure to connect to a public node from https://github.com/hyperboria/peers. Not all of them work, but most do. trn's tokyo node is known to work.
4. netcat.

## Answer
FLAG{d3centra1ise_t3h_interwebz}
