#include <stdio.h>
int n, a[101], tmp[101];

void mergeSort(int lt, int rt)
{
    int mid;
    int p1, p2, p3;
    if (lt < rt)
    {
        mid = (lt + rt) / 2;
        mergeSort(lt, mid);
        mergeSort(mid+1, rt);
        // 왼쪽, 오른쪽 subtree 를 우선 처리하고 그 다음에 자기 작업을 하는
        // 후위순회 방식의 dfs 다. 
        p1 = lt; p2 = mid+1; p3 = lt;
        while (p1 <= mid && p2 <= rt)
        {
            if (a[p1] < a[p2]) tmp[p3++] = a[p1++];
            else tmp[p3++] = a[p2++];            
        }
        while (p1 <= mid) tmp[p3++] = a[p1++];
        while (p2 <= rt) tmp[p3++] = a[p2++];
        for (size_t i = lt; i <= rt; i++)
        {
            a[i] = tmp[i];
        }
    }
}

int main()
{
    scanf("%d", &n);
    for (size_t i = 1; i <= n; i++)
    {
        scanf("%d", &a[i]);
    }
    mergeSort(1, n);
    for (size_t i = 1; i <= n; i++)
    {
        printf("%d ", a[i]);
    }
    
    return 0;
}