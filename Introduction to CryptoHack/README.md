### Summary

* To convert a hex __h__ to bytes use : bytes.fromhex(h).

* To convert a string __str__ to bytes use : bytes(str, "utf-8").

* To convert from long to bytes, or vice-versa use the functions long_to_bytes and bytes_to_long of Crypto.Util.number module like to following way.

* To do __xor operation__ between two variables, ensure to convert these variables to bytes first.

* You can use to function __xor__ from the __pwntools__ module.
