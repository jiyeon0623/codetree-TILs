#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int age1, age2;
    char per1, per2;

    scanf("%d %c", &age1, &per1);
    scanf("%d %c", &age2, &per2);

    if ((age1 >=19 && per1 == 'M') || (age2 >=19 && per2 == 'M')){
        printf("%d", 1);
    }
    else{
        printf("%d", 0);
    }
    return 0;
}