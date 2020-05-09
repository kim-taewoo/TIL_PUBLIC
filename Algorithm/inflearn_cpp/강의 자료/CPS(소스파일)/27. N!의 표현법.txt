#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
	freopen("input.txt", "rt", stdin);
	int n, i, j, tmp;
	scanf("%d", &n);
	vector<int> ch(n+1);
	for(i=2; i<=n; i++){
		tmp=i;
		j=2;
		while(1){
			if(tmp%j==0){
				ch[j]++;
				tmp=tmp/j;
			}
			else j++;
			if(tmp==1) break;
		}
	}
	printf("%d! = ", n);
	for(j=2; j<=n; j++){
		if(ch[j]!=0) printf("%d ", ch[j]);
	}
	return 0;
}
				
		
	