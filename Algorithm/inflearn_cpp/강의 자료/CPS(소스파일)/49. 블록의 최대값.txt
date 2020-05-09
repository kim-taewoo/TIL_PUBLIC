#include<stdio.h>
int a[11][11], b[11];
int main(){
	freopen("input.txt", "rt", stdin);
	int n, i, j, sum=0;
	scanf("%d", &n);
	for(i=1; i<=n; i++)
		scanf("%d", &b[i]);
	for(i=1; i<=n; i++){
		for(j=1; j<=n; j++){
			a[j][i]=b[i];
		}
	}
	for(i=n; i>=1; i--)
		scanf("%d", &b[i]);
	for(i=1; i<=n; i++){
		for(j=1; j<=n; j++){
			if(a[i][j]>b[i]) a[i][j]=b[i];
		}
	}
	for(i=1; i<=n; i++){
		for(j=1; j<=n; j++){
			sum+=a[i][j];
		}
	}
	printf("%d\n", sum);
	return 0;
}