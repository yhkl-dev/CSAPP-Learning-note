awk 'BEGIN {max = 0} {if ($6+0 > max+0) max=$6} END {print "Max=", max, "User:", $1}' ~/weibo_freshdata.2020-04-10
