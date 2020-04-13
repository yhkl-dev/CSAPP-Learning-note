#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool isValid(char *s) {
	int length=0;//定义字符串长度
	while(*(s+length))length++;//获取字符串长度
	char* ptr=(char*)malloc(length/2);//分配内存空间
	memset(ptr,0,length/2);//初始化内存空间
	int i,a=0;
	for(i=0;i<length;i++)
	{
    		if((*(s+i)=='(')||(*(s+i)=='{')||(*(s+i)=='[')) {
        		a++;
			*(ptr+a)=*(s+i);
		}  //'('与')'的ASCII值差1，'['与']'，'{'与'}'的ASCII值差2
		else if((*(s+i)==(*(ptr+a)+1))||(*(s+i)==(*(ptr+a)+2))) {
			a--;
		}
    		else return 0;
	}
	if(a) {
    		return 0;
	}
	return 1;
}
