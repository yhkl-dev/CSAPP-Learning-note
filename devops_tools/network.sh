# 
# No: 序号
# Device: 网卡名称
# Status: 网卡状态
# Speed: 网卡速度
# Type: 网卡类型(光口： FIBRE 电口：TP)
# IPADDR: ip地址
# MASK: 掩码
# Bcast: 组播地址

(string='|%-3s|%-18s|%-10s|%-10s|%-10s|%-16s|%-16s|%-16s|';                                               
br="`echo $string|grep -Eo '[0-9]+'|awk '{s=s+$1}END{s=s+NR;for(i=0;i<=s;i++){printf "-"};print""}';`";  
printf1(){ printf "$string\n"  NO  Device  Status  Type  Speed  Ipaddr  Mask  Bcast; };                 
printf2(){ printf "$string\n" $NO $DEVICE $STATUS $TYPE $SPEED $IPADDR $MASK $BCAST; };                 
echo $br;printf1;echo $br;                                                                               
NO=0;                                                                                                    
for i in `ip a|awk -F ':' '/^[0-9]/{print $2}'|sort`; do                                                 
  DEVICE=$i;                                                                                             
  STATUS=`ip a|grep ":.$i:"|awk '{print /LOWER_UP/?"UP":"DOWN"}'`;                                       
  TYPE=`  ethtool $i |grep 'Supported ports' |sed 's/]//g' |awk -F '[' '{print $2}'|sed 's/ //g'`;       
  SPEED=` ethtool $i |awk '/Speed/{print $NF}'`;                                                         
  IPADDR=`ifconfig $i |grep -Eo '([0-9]+\.){3}[0-9]{1,3}'|awk 'NR==1'`;                                 
  MASK=`  ifconfig $i |grep -Eo '([0-9]+\.){3}[0-9]{1,3}'|awk '/^255/'`;                                
  BCAST=` ifconfig $i |grep -Eo '([0-9]+\.){3}[0-9]{1,3}'|awk 'NR>1&&!/^255/'`;                         
  [ "x"$STATUS == "x" ] && STATUS='-';                                                                   
  [ "x"$TYPE   == "x" ] && TYPE='-';                                                                     
  [ "x"$SPEED  == "x" ] && SPEED='-';                                                                    
  [ "x"$IPADDR == "x" ] && IPADDR='-';                                                                   
  [ "x"$BCAST  == "x" ] && BCAST='-';                                                                    
  [ "x"$MASK   == "x" ] && MASK='-';                                                                     
  printf2;                                                                                               
  NO=`echo $NO|awk '{print $1+1}'`;                                                                      
done 2>/dev/null;                                                                                        
echo $br;                                                                                                
route -n|grep ^0.0.0.0|awk '{print "GATEWAY: ",$2," "$NF}';                                              
echo $br;                                                                                                
)
