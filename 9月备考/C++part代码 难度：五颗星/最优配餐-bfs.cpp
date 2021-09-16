//CCF - 最优配餐
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
} C[N], Node; //C存储客户信息 走多少步路

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
	//从客户出发 找最近的分店？
	for (int i = 0; i < k; i++) {
		// C[i]作为st 寻找最近路线
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
		g[x][y] = 0;//分店记为0
	}
	for (int i = 0; i < k; i++) {
		cin >> x >> y >> z;
		C[i].x = x, C[i].y = y, C[i].step = 0;
		g[x][y] = z;//客户记为量
	}
	for (int i = 0; i < d; i++) {
		cin >> x >> y;
		g[x][y] = INF; //不可达记为INF
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
本题思路：求出分店到各个点的最短距离
根据最短距离求出最少成本
输出成本
bfs思路：
源点入队
当队列不为空时：
	从队列中取出队首元素
	访问队首元素 将其可达的点放入队列中
	队首元素出队

*/