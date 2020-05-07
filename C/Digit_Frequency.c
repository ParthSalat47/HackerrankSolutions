#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

  char *str = malloc(1024 * sizeof(char));
  char *i = malloc(10 * sizeof(char));
  
  

  for(char x='0';x<='9';x++)
  {
    *(i+(int)x-48) = x;
  }
  char temp = *(i);
  //printf("%c hi",temp);

  //printf("%d",*(i+2));

  scanf("%s",str);
  //printf("%s",str);

  char j;
  int run = 0,result=0;
  int count = 0,y;
  int compare = 0;
  int len = strlen(str);
  
  //char h ='0';
  //printf("%d\n\n",h);

  for(y=0;y<=9;y++)
  {
    count = 0,run=0;
    for(j=*str;run<len;run++)
    {
      //compare = (int)i - 97;
      //printf("%c\t",j);
      
      //printf("%d ",result);
      if(temp==j)
      {
        count++;
        //printf("%d ",count);
      }
      
      j=*(str+run+1);
      //printf("%c\t",j);
    }
    printf("%d ",count);
    temp=*(i+y+1);
    //printf("%c\n",temp);
    
  }




    return 0;
}
