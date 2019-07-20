\rm -rf dist
mkdir dist
bazel build --platforms=@io_bazel_rules_go//go/toolchain:linux_amd64 //guess/...
mkdir dist/guess_client
cp bazel-bin/guess/guess_client/linux_amd64_pure_stripped/guess_client dist/guess_client/
cp -r guess/guess_server dist/
tar czvf dist.tgz dist/
