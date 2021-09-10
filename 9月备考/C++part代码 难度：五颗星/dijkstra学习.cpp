//Dijstra算法
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;

struct Node {
	int v, dis;
	Node(int _v, int _dis) {
		v = _v;
		dis = _dis;
	}
};


const int MAXV = 1000;
const int INF = 0x3fffffff;
int n, m, st, ed;
vector<Node> Adj[MAXV];
int d[MAXV];
bool vis[MAXV];//是否访问过

void dijkstra(int st) { //起点
	fill(d, d + MAXV, INF);
	d[st] = 0;
	memset(vis, false, sizeof vis);

	for (int i = 0; i < n; i++) {
		int u = -1; // 找出一个最短的地点攻占
		int min_distance = INF;
		for (int j = 0; j < n; j++) {
			if (vis[j] == false && d[j] < min_distance) {
				min_distance = d[j];
				u = j;
			}
		}
		if (u == -1) {
			//如果找不到小于INF的d[u]，说明剩下的节点与s不连通
			return;
		}
		vis[u] = true;
		for (int j = 0; j < Adj[u].size(); j++) {
			int v = Adj[u][j].v;
			if (vis[v] == false && d[u] + Adj[u][j].dis < d[v]) {
				d[v] = d[u] + Adj[u][j].dis;
			}
		}
	}
}


int main() {
	cin >> n >> m >> st >> ed; //n个顶点 m条边
	int a, b, wt;
	for (int i = 0; i < m; i++) {
		cin >> a >> b >> wt;
		Adj[a].push_back(Node(b, wt));
		//Adj[b].push_back(Node(a, wt));
	}

	dijkstra(st);
	for (int i = 0; i < n; i++) {
		cout << d[i] << endl;
	}
	return 0;
}

//测试数据
//6 8 0 1
//0 1 1
//0 2 4
//0 3 4
//1 3 2
//2 5 1
//3 2 2
//3 4 3
//4 5 3