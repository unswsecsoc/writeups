rm foo2.*

echo 'encrypting...'
echo -e 'hi' | ./timeless foo.txt
echo ''

mv foo.txt.tl foo2.txt.tl

echo 'decrypting...'
echo -e 'hi' | ./timeless foo2.txt.tl
echo ''

diff foo.txt foo2.txt
