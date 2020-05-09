#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int stack[100], top=-1;

void push(int x){
	stack[++top]=x;
}
int pop(){
	return stack[top--];
}

int main(){
	freopen("input.txt", "rt", stdin);
	int n, k;
	char str[20]="0123456789ABCDEF";
	scanf("%d %d", &n, &k);
	while(n>0){
		push(n%k);
		n=n/k;
	}
	while(top!=-1){
		printf("%c", str[pop()]);
	}	
	return 0;
}




#include<stdio.h>
#include<vector>
#include<stack>
#include<algorithm>
using namespace std;		
int main(){
	freopen("input.txt", "rt", stdin);
	int n, k;
	stack<int> s;
	char str[20]="0123456789ABCDEF";
	scanf("%d %d", &n, &k);
	while(n>0){
		s.push(n%k);
		n=n/k;
	}
	while(!s.empty()){
		printf("%c", str[s.top()]);
		s.pop();
	}	
	return 0;
}