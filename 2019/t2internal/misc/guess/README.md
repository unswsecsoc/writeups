# Guess

A Number guessing game CTF challenge.

## Vulnerability

Weak pseudo-random number

You also need to reverse engineer gRPC/Protobuf traffic to solve this.

Alternatively, crack the provided binary to disable limits.

## Building

Use Blaze.

```
bazel build //guess/...
bazel build //solver
```

## Write-Up

1. read server source code
2. run client and tcpdump
3. analyze grpc traffic to know id of protobuf variables
4. generate "random" sequence dictionary
5. write script and profit

## PoC

There's a working solver at //solver

## Author

[Adam Yi](https://www.adamyi.com)
