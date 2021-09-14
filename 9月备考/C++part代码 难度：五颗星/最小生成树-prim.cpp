//最小生成树
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

const int INF = 0x3fffffff;
const int MAXV = 10010;
struct Node {
	int v, dis;
	Node(int _v, int _dis) {
		v = _v;
		dis = _dis;
	}
};
int n, m, st;
int d[MAXV];//存储顶点Vi与集合S的最短距离  范围相对于Dijkstra算法中d减小了
//【Dijkstra中d的含义是起点st到顶点Vi的最短距离】
vector<Node> Adj[MAXV];

bool vis[MAXV];//存储顶点是否被拜访过
int prim() {
	memset(vis, false, sizeof vis);
	fill(d, d + MAXV, INF);
	d[0] = 0;
	int ans = 0;//记录存放最小生成树的边权之和
	for (int i = 0; i < n; i++) {
		int u = -1, MIN = INF; //寻找d[u]最小且未被访问过的标号
		for (int j = 0; j < n ; j++) {
			if (vis[j] == false && d[j] < MIN) {
				MIN = d[j];
				u = j;
			}
		}
		//cout << u << endl;
		if (u == -1)
			return -1;
		vis[u] = true;
		ans += d[u];
		for (int j = 0; j < Adj[u].size(); j++) { //遍历所有与u相连的顶点v
			int v = Adj[u][j].v;
			int dis = Adj[u][j].dis;
			if (vis[v] == false && d[v] > dis) {
				d[v] = Adj[u][j].dis;
			}
		}
//		for (int j = 0; j < n; j++) {
//			cout << d[j] << endl;
//		}
	}
	return ans;
}

int main() {
	cin >> n >> m;
	int a, b, c;
	for (int i = 0; i < m; i++) {
		cin >> a >> b >> c;
		Adj[a].push_back(Node(b, c));
		Adj[b].push_back(Node(a, c));
	}
//	for (int i = 0; i < n; i++) {
//		cout << i << endl;
//		for (int j = 0; j < Adj[i].size(); j++) {
//			cout << Adj[i][j].v << " " << Adj[i][j].dis << endl;
//		}
//	}
	int ans = prim();
	cout << ans << endl;
	return 0;
}

/*
算法伪代码：
初始化数组vis，d
for(循环n次):
	u = 使d[u]最小的还未被访问过的顶点标号；
	记u已经被访问过；
	for 从u出发可以到达的顶点v:
		如果v没有被访问，并且d[v]<d[u]+dis:
			d[v] = G[u][v]
6 10
0 1 4
0 4 1
0 5 2
1 2 6
1 5 3
2 3 6
2 5 5
3 4 4
3 5 5
4 5 3
结果：15
*/