#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int a;
    scanf("%d", &a);

    if (a<0){
        printf("ice");
    }
    else if (0<a<100){
        printf("water");
    }
    else {
        printf("vapor");
    }
    return 0;
}