//  c언어로 array 연습
//  Copyright © 2019 spesdev. All rights reserved.

#include <stdio.h>

int main(void)
{
    // insert code here...
    #define N 5
    
    int i;
    int a[N];
    
    for(i=0; i<N; i++)
    {
        printf("a[%d] : ", i);
        scanf("%d", &a[i]);
    }
    
    puts("각 요소의 값");
    
    for (i=0; i<N; i++)
    {
        printf("a[%d] = %d\n", i, a[i]);
    }
    return 0;
}
