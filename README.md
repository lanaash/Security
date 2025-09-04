# Regex debugging

    apt-get install libregexp-debugger-perl

Run rxrx and supply 

    /[regex] & 'string'

Then m to step thru the regex operation


# Perl one-liners


## Remove newlines
```
perl -pe 's/\n//' file.txt
```
## Replace string in file & save backup copy
```
perl -p -i.bak -e 's/old/new/g' orig
```
