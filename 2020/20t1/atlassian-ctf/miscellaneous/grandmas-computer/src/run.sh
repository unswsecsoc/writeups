docker run --rm -it $(grep "Successfully built" buildlog | cut -d ' ' -f 3)
