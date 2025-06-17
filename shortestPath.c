#include <stdio.h>
#include <conio.h>

int x[50][50];
int d[50][50];

void apsp(int n) {
    int i, j, k, q;

    for (i = 1; i <= n; i++)
        for (j = 1; j <= n; j++)
            x[i][j] = d[i][j];

    printf("\nX0:\n");
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++)
            printf("%d\t", x[i][j]);
        printf("\n");
    }

    for (k = 1; k <= n; k++) {
        printf("\nX%d:\n", k);
        for (i = 1; i <= n; i++) {
            for (j = 1; j <= n; j++) {
                q = x[i][j] < (x[i][k] + x[k][j]) ? x[i][j] : (x[i][k] + x[k][j]);
                x[i][j] = q;
            }
        }

        for (i = 1; i <= n; i++) {
            for (j = 1; j <= n; j++)
                printf("%d\t", x[i][j]);
            printf("\n");
        }
    }
}

int main() {
    int n, i, j;
    printf("\nEnter the number of nodes: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++)
        for (j = 1; j <= n; j++) {
            printf("\nd[%d][%d]: ", i, j);
            scanf("%d", &d[i][j]);
        }

    apsp(n);

    return 0;
}
