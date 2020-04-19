echo "transmit"
awk -F "\t" '{print $5 | "sort -r -n " } END{print}' ~/weibo_freshdata.2020-04-10 |head -10

echo "comment"
awk -F "\t" '{print $6 | "sort -r -n " } END{print}' ~/weibo_freshdata.2020-04-10 |head -10
