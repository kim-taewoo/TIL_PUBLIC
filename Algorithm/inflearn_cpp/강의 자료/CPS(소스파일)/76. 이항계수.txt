#include<stdio.h>
using namespace std;
int dy[21][21];

int C(int n, int r){
	if(dy[n][r]>0) return dy[n][r];
	if(n==r || r==0) return 1;
	else return dy[n][r]=C(n-1, r)+C(n-1, r-1);
}

int main(){
	freopen("input.txt", "rt", stdin);
	int n, r;
	scanf("%d %d", &n, &r);
	printf("%d\n", C(n, r));
	return 0;
}