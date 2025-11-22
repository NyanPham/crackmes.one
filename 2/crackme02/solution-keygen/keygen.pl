#!/usr/bin/perl
#sadegh<dot>ahm<at>gmail<dot>com
sub randch{return shift(@_) if defined $_[0];chr(65+rand(60));}
print randch.randch.randch."1003".randch."08X32".randch.($x=randch).($y=randch).randch($x).randch($y)."-da\n";

