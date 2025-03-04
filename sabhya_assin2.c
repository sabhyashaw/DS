#include<stdio.h>
#define max 10
int a[11]={10,14,19,-26,27,-31,33,35,24,44,1};
void merging (int low,int mid, int high)
{

    int l1,l2,i,b[100];
    for(l1=low,l2=mid+1, i=low; l1<=mid && l2<=high;i++){
        if(a[l1]<=a[l2])
            b[i]=a[l1++];
        else
        b[i]=a[l2++];
        }
    while(l1<=mid)
        b[i++]=a[l1++];
    while(l2<=high)
        b[i++]=a[l2++];
    for(i=low;i<=high;i++)
        a[i]=b[i];
}
void merge_sort(int low, int high){
int mid;
if(low<high){
    mid=(low+high)/2;
    merge_sort(low,mid);
    merge_sort(mid+1,high);
    merging(low,mid,high);
}
}
int main()
{

    int i;
    printf("list before sorting \n");
    for(i=0;i<=max;i++)
        printf(" %d",a[i]);
    merge_sort(0,max);
    printf("\nlist after sorting\n");
    for(i=0;i<=max;i++)
        printf(" %d",a[i]);
    return 1;
}
