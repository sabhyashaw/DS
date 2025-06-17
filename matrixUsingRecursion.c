#include <stdio.h>
#include <limits.h>

int MatrixChainOrder(int p[], int i, int j) {
    int k;
    int min = INT_MAX;
    int count;

    if (i == j)
        return 0;

    for (k = i; k < j; k++) {
        count = MatrixChainOrder(p, i, k)
              + MatrixChainOrder(p, k + 1, j)
              + p[i - 1] * p[k] * p[j];
        if (count < min)
            min = count;
    }

    return min;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Minimum number of multiplications is %d\n",
           MatrixChainOrder(arr, 1, n - 1));

    return 0;
}
