#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int sc;
    scanf("%d", &sc);
    if (sc >=80){
        printf("pass");
    }
    else{
        printf("%d more score", 80-sc);
    }
    return 0;
}