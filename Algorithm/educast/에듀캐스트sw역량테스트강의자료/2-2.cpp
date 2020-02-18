#include <iostream>
using namespace std;

char ary[100][100];

// 위치 p부터 len 만큼의 길이의 문자열이 회문인지 판단하는 함수
bool isPalindrome(char * p, int len)
{
	for (int i = 0; i < (len + 1) / 2; i++)
		if (*(p + i) != *(p + len - 1 - i))
			return false;

	return true;
}


int getMaxPalindrome(char ary[][100])
{
	int max = 0; //현재까지 나온 최대 회문의 길이를 저장함.

	for (int i = 0; i < 100; i++)
		for (int j = 0; j < 100; j++)
			for (int k = 100 - j; k > max; k--)  //가능한한 최대 길이의 문자열부터 회문인지를 검사
				if (isPalindrome(&ary[i][j], k))
				{
					if (max < k) max = k;
					break;
				}

	return max;
}

void main()
{
	int ans = 0;
	freopen("input.txt", "r", stdin); // 리소스 파일 input.txt 파일로부터 input을 읽어오도록 설정 -> 불필요시 주석처리 필요

	for (int tc = 1; tc <= 10; tc++)
	{
		int n;
		cin >> n;

		for (int i = 0; i < 100; i++)
			for (int j = 0; j < 100; j++)
				cin >> ary[i][j];

		ans = getMaxPalindrome(ary);

		// (x,y) <-> (y,x) swap  =>  행과 열이 swap 됨.
		for (int i = 0; i < 100; i++)
			for (int j = 0; j < 100; j++)
				if (i < j)
				{
					char t = ary[i][j];
					ary[i][j] = ary[j][i];
					ary[j][i] = t;
				}

		ans = getMaxPalindrome(ary) < ans ? ans : getMaxPalindrome(ary);

		cout << "#" << tc << " " << ans << endl;
		ans = 0;
	}
}
