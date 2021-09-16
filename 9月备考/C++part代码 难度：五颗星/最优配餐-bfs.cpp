//CCF - �������
#include <iostream>
#include <queue>

using namespace std;
const int N = 1010;
const int INF = 0x3fffffff;
int g[N][N];
int n, m, k, d;

bool inq[N][N] = {false};


int dx[] = {0, 0, 1, -1}, dy[] = {1, -1, 0, 0};

struct node {
	int x, y;
	int step;
} C[N], Node; //C�洢�ͻ���Ϣ �߶��ٲ�·

bool test(int x, int y) {
	if (x <= 0 || x > n || y <= 0 || y > n)
		return false;
	if (inq[x][y] == true)
		return false;
	if (g[x][y] == INF)
		return false;
	return true;
}

int bfs() {
	int ans = 0;
	//�ӿͻ����� ������ķֵꣿ
	for (int i = 0; i < k; i++) {
		// C[i]��Ϊst Ѱ�����·��
		queue<node> q;
		q.push(C[i]);
		while (!q.empty()) {
			node top = q.front();
			q.pop();
			if (g[top.x][top.y] == 0) {
				//cout << top.step << " " << g[C[i].x][C[i].y] << endl;
				ans = ans + top.step * g[C[i].x][C[i].y];
				break;
			}
			for (int j = 0; j < 4; j++) {
				int newX = top.x + dx[j];
				int newY = top.y + dy[j];
				if (test(newX, newY)) {
					Node.x = newX, Node.y = newY, Node.step = top.step + 1;
					q.push(Node);
				}
			}
		}
	}
	return ans;
}

int main() {
	cin >> n >> m >> k >> d;
	int x, y, z;
	fill(g[0], g[0] + N * N, -1);
	for (int i = 0; i < m; i++) {
		cin >> x >> y;
		g[x][y] = 0;//�ֵ��Ϊ0
	}
	for (int i = 0; i < k; i++) {
		cin >> x >> y >> z;
		C[i].x = x, C[i].y = y, C[i].step = 0;
		g[x][y] = z;//�ͻ���Ϊ��
	}
	for (int i = 0; i < d; i++) {
		cin >> x >> y;
		g[x][y] = INF; //���ɴ��ΪINF
	}
//	cout << endl;
//	for (int i = 0; i < n; i++) {
//		for (int j = 0; j < n; j++) {
//			cout << g[i][j] << " ";
//		}
//		cout << endl;
//	}
	int ans = bfs();
	cout << ans << endl;
	return 0;
}
/*
����˼·������ֵ굽���������̾���
������̾���������ٳɱ�
����ɱ�
bfs˼·��
Դ�����
�����в�Ϊ��ʱ��
	�Ӷ�����ȡ������Ԫ��
	���ʶ���Ԫ�� ����ɴ�ĵ���������
	����Ԫ�س���

*/