# Verification key
## Flavour text
This cat likes to copy you. Can you get it to copy something else?
## Solution
This is a buffer overflow challenge with a stack canary, so we'll need
to make sure the canary remains unchanged.

Set the 21st character to '%' when you enter the string. 
Alternatively, spam some '%'s. About 30 should do.

## Flag
FLAG{ginger_tabby_black_persian_neko}
