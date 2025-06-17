#include <stdio.h>

int a[11] = {10, 14, 19, -26, 27, -31, 33, 35, 24, 44, 1};

void merge(int low, int mid, int high) {
    int i, j, k, b[11];
    i = low;
    j = mid + 1;
    k = low;

    while (i <= mid && j <= high) {
        if (a[i] <= a[j]) {
            b[k] = a[i];
            i++;
        } else {
            b[k] = a[j];
            j++;
        }
        k++;
    }

    while (i <= mid) {
        b[k] = a[i];
        i++;
        k++;
    }

    while (j <= high) {
        b[k] = a[j];
        j++;
        k++;
    }

    for (i = low; i <= high; i++) {
        a[i] = b[i];
    }
}

void mergeSort(int low, int high) {
    int mid;
    if (low < high) {
        mid = (low + high) / 2;
        mergeSort(low, mid);
        mergeSort(mid + 1, high);
        merge(low, mid, high);
    }
}

int main() {
    int i, n = 11;

    mergeSort(0, n - 1);

    printf("Sorted array:\n");
    for (i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }

    printf("\n");

    return 0;
}
