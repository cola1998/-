//��¼������bfs
#include <iostream>
#include <cstring>
#include <queue>
using namespace std;
const int N = 100;

struct node {
	int x, y;
	int step;//��Դ�㵽��λ����С������������
} S, T, Node;

int n, m;










char maze[N][N];//�Թ���Ϣ
bool inq[N][N] = {false}; //��¼�Ƿ���ʹ�
int bx[] = {0, 0, 1, -1}, by[] = {1, -1, 0, 0};

bool test(int x, int y) {
	//���λ��(x,y)�Ƿ���Ч
	if (x < 0 || x >= n || y < 0 || y >= n)
		return false;
	if (maze[x][y] == '*')
		return false;
	if (inq[x][y] == true)
		return false;
	return true;
}

int bfs() {
	queue<node> q;
	q.push(S);
	//inq[S.x][S.y] = true;
	while (!q.empty()) {
		node top = q.front();
		q.pop();
		if (top.x == T.x && top.y == T.y)
			return top.step;
		for (int i = 0; i < 4; i++) {
			int a = top.x + bx[i];
			int b = top.y + by[i];
			if (test(a, b)) {
				Node.x = a, Node.y = b, Node.step = top.step + 1;
				q.push(Node);
				inq[a][b] = true;
			}
		}
	}
	return -1;
}

int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> maze[i][j];
		}
	}
	cin >> S.x >> S.y >> T.x >> T.y; // ����յ�����
	S.step = 0;
	int res = bfs();
	cout << res;
	return 0;
}
/*
5 5
.....
.*.*.
.*S*.
.***.
...T*
2 2 4 3
*/