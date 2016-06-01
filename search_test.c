#include <stdio.h>

int binSearch(int a[], int length, int x) {
    int left = 0;
    int right = length - 1;
    int mid;
    int pos = -1;
    int n = 0;

    while (left <= right && pos == -1) {
        n++;
        mid = (left + right) / 2;
        printf("%d回目の処理:左端 = %d, 右端 = %d, 真ん中 = %d\n", n, left, right, mid);
        if (a[mid] == x) {
            pos = mid;
        } else if (a[mid] > x) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return pos;
}


int main() {
    int a[10] = { 13, 27, 33, 39, 48, 52, 61, 65, 74, 86 };
    int x = 61;
    printf("検索結果 = %d\n", binSearch(a, 10, x));

    return 0;
}
