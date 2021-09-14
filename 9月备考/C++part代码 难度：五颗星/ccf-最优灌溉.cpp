//csp 201412-4 最优灌溉
#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

struct Node {
	int v, dis;
	Node(int _v, int _dis) {
		v = _v;
		dis = _dis;
	}
};
const int MAXV = 10010;
const int INF = 0x3fffffff;

vector<Node> Adj[MAXV];
int n, m;
int d[MAXV];
bool vis[MAXV] = {false};

int prim() {
	int count = 0;//记录最小费用
	fill(d, d + MAXV, INF);
	d[1] = 0;
	for (int i = 0; i < n; i++) {
		//遍历n次
		int u = -1, MIN = INF; //寻找最小的未被访问过的序号
		for (int j = 1; j <= n; j++) {
			if (vis[j] == false && d[j] < MIN) {
				MIN = d[j];
				u = j;
			}
		}
		if (u == -1)
			return -1;
		vis[u] = true;
		count = count + d[u];
		for (int j = 0; j < Adj[u].size(); j++) {
			int v = Adj[u][j].v;
			int dis = Adj[u][j].dis;
			if (vis[v] == false && dis < d[v]) {
				d[v] = dis;
			}
		}
	}
	return count;
}

int main() {
	cin >> n >> m;
	int a, b, c;
	for (int i = 0; i < m; i++) {
		cin >> a >> b >> c;
		Adj[a].push_back(Node(b, c));
		Adj[b].push_back(Node(a, c));
	}
	int res = prim();
	if (res != -1)
		cout << res << endl;
	else
		cout << "-1" << endl;
	return 0;
}