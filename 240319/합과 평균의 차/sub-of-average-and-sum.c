#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int a,b,c, avg;
    scanf("%d %d %d", &a, &b, &c);
    avg = a+b+c;
    printf("%d\n%d\n%d", avg, (avg)/3, avg-(avg)/3);
    return 0;
}