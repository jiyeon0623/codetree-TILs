#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int a;
    scanf("%d", &a);

    if (a%3 == 0 || a%5 == 0){
        printf("%d", 1);
    }
    else{
        printf("%d", 0);
    }
    return 0;
}