//
//  array_2.c
//  array
//
//  Created by 임슬기 on 17/09/2019.
//  Copyright © 2019 spesdev. All rights reserved.
//

#include "array_2.h"

int main(void)
{
    int i;
    int a[5] = {10, 20, 30, 40, 50};
    int na = sizeof(a) / sizeof(a[0]);
    
    printf("배열 a의 요소 개수는 %d 입니다.\n", na);
    
    for(i=0; i<na; i++)
    {
        printf("a[%d] = %d\n", i, a[i]);
    }
    
    return 0;
}
