#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int a,b,c;
    scanf("%d %d %d", &a, &b, &c);
    if (a<=b && a<=c){
        printf("%d ", 1);
    }
    else{
        printf("%d ", 0);
    }

    if (a == b && b == c && a==c){
        printf("%d ", 1);
    }
    else{
        printf("%d ", 0);
    }
    return 0;
}