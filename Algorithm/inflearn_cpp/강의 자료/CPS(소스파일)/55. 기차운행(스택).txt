#include<stdio.h>
#include<stack>
#include<vector>
using namespace std;			
int main(){
	//freopen("input.txt", "rt", stdin);
	stack<int> s;
	int i, j=1, n, m;
	scanf("%d", &n);
	vector<char> str;
	for(i=1; i<=n; i++){
		scanf("%d", &m);
		s.push(m);
		str.push_back('P');
		while(1){
			if(s.empty()) break;
			if(j==s.top()){
				s.pop();
				j++;
				str.push_back('O');
			}
			else break;
		}
	}
	if(!s.empty()) printf("impossible\n");
	else{
		for(i=0; i<str.size(); i++) printf("%c", str[i]);
	}
	return 0;
}

