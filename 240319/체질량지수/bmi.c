#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int a,b,bmi;
    scanf("%d %d", &a, &b);
    bmi = b*100*100/(a*a);
    printf("%d\n", bmi);
    if (bmi >=25){
        printf("Obesity");
    }
    return 0;
}