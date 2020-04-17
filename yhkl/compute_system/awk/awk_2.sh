echo "transmit"
awk -F "\t" '{print  | "sort -r -n -k 5" } END{print}' ~/weibo_freshdata.2020-04-10 |head -10

echo "comment"
awk -F "\t" '{print  | "sort -r -n -k 6" } END{print}' ~/weibo_freshdata.2020-04-10 |head -10
