#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;	
void D(int x){
	if(x>7) return;
	else{
		printf("%d ", x);
		D(x*2);
		D(x*2+1);
	}
}	
int main(){
	freopen("input.txt", "rt", stdin);
	D(1);
	return 0;
}