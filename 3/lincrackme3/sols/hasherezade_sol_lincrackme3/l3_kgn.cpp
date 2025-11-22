/*
 * Solution for: adrianbn's lincrackme3
 * Coded by hasherezade
 * */

#include <cstdlib>
#include <iostream>

using namespace std;

int Sum1,Sum2, Sum3, Sum4;

int getSum1(){
    int s1=0;
    while((s1=(rand()%(23-7))+7)%2==0)
    ;
    return s1;
}

int getSum2(){
    int s2=0;
    while((s2=(rand()%(35-1))+1)%2==0)
    ; 
    return s2;	
}

int getSum4(int Sum1,int Sum2){
    int c=((Sum1+Sum2)/2)+1;
    int s4=0;
    while((s4=(rand()%c))%2==0)
    ;
    return s4;
}

bool checkup(int Sum1,int Sum2,int Sum3,int Sum4){  
    if(Sum1>36||Sum2>36||Sum3>36||Sum4>36) return false; //sum cannot be greater than 9+9+9+9=36
    if(Sum1<0||Sum2<0||Sum3<0||Sum4<0) return false; //and lower than 0+0+0+0=0
    //conditions from the keyCheck procedure:
    if(Sum1+Sum2!=(2*(Sum3+Sum4)) )  return false;
    if(Sum2<=Sum3) return false;
    if((Sum1+Sum4)%2 != 0) return false;
    if(Sum1<=5||Sum1>24) return false;
    if (Sum4 %2 == 0) return false;
    return true;
}

bool generateSums(){
    Sum1=getSum1();
    Sum2=getSum2();
    do{
    	Sum4=getSum4(Sum1,Sum2);
    	Sum3=(Sum1+Sum2)/2-Sum4;
    }while(Sum2<=Sum3);
    return checkup(Sum1, Sum2, Sum3, Sum4);
}

void fillChunk(char buf[4],int sum){
    for(int i=0;i<4;i++)
        buf[i]='0';
    while(sum>0){
        int i=rand()%4;
        if(buf[i]<'9'){
            buf[i]++;
            sum--;
        }
    }
}

int main(int argc, char *argv[])
{
    srand((int)time(NULL));
    char a1[4];
    char a2[4];
    char a3[4];
    char a4[4];

    while(!generateSums())
    ;
    for(int i=0;i<10;i++){
        fillChunk(a1,Sum1);
        fillChunk(a2,Sum2);
        fillChunk(a3,Sum3);
        fillChunk(a4,Sum4);
        printf("%c%c%c%c-%c%c%c%c-%c%c%c%c-%c%c%c%c\n",
            a1[0],a1[1],a1[2],a1[3],
            a2[0],a2[1],a2[2],a2[3],
            a3[0],a3[1],a3[2],a3[3],
            a4[0],a4[1],a4[2],a4[3]
        ); 
    }
    return EXIT_SUCCESS;
}
