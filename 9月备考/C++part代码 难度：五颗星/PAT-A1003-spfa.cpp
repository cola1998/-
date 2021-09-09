//spfa  求单源最短路径的算法
/*
n个点 m条边有向图 且边权可能为负
求1-n的最短距离
*/
#include <iostream>
#include <queue>
#include <set>
using namespace std;
const int INF = 0x3fffffff;
const int MAXV = 501;

struct Node {
	int v, dis;
	Node(int _v, int _dis) {
		v = _v;
		dis = _dis;
	}
};

vector<Node> Adj[MAXV];
int n, m, st, ed; // n个顶点，m条边，st起点，ed终点
int d[MAXV], weight[MAXV]; //dis数组记录源点到点i的最短距离 weight记录点权
int num[MAXV], w[MAXV]; //num数组记录最短路径条数，w记录路径的最大点权
int cnt[MAXV];//记录源点入队次数
bool inq[MAXV];  //顶点是否在队列中
set<int> pre[MAXV];

bool spfa(int st) {
	fill(d, d + MAXV, INF);
	d[st] = 0;
	memset(num, 0, sizeof num);
	num[st] = 1;
	memset(w, 0, sizeof w);
	w[st] = weight[st];
	memset(inq, false, sizeof inq);
	memset(cnt, 0, sizeof cnt);
	cnt[st] = 1;
	queue<int> Q;
	Q.push(st);
	inq[st] = true;

	while (!Q.empty()) {
		int u = Q.front(); //队首编号为u
		Q.pop();//出队
		inq[u] = false;

		//遍历u的所有邻接边
		for (int j = 0; j < Adj[u].size(); j++) {
			int v = Adj[u][j].v;
			int dis = Adj[u][j].dis;

			//松弛操作
			if (d[u] + dis < d[v]) {
				d[v] = d[u] + dis;
				w[v] = w[u] + weight[v];
				pre[v].clear();
				pre[v].insert(u);
				num[v] = num[u];
				if (!inq[v]) { //如果v不在队列里，将其加入队列中
					Q.push(v);
					inq[v] = true;
					cnt[v]++;  //v的入队次数加1
				}
			} else if (d[u] + dis == d[v]) {
				if (w[u] + weight[v] > w[v]) {
					w[v] = w[u] + weight[v];
				}
				pre[v].insert(u);
				num[v] = 0;
				set<int>::iterator it;
				for (it = pre[v].begin(); it != pre[v].end(); it++) {
					num[v] += num[*it];
				}
				if (!inq[v]) { //无论w[v]是否改变，num[v]都可能改变，所以要入队？？？
					Q.push(v);
					inq[v] = true;
					cnt[v]++;  //v的入队次数加1
				}
			}
			if (cnt[v] >= n)
				return false; //v的入队次数大于n-1，说明可能存在负环
		}
	}
	return true;
}

int main() {
	cin >> n >> m >> st >> ed;
	for (int i = 0; i < n; i++) {
		cin >> weight[i];
	}
	int a, b, wt;
	for (int i = 0; i < m; i++) {
		cin >> a >> b >> wt;
		Adj[a].push_back(Node(b, wt));
		Adj[b].push_back(Node(a, wt));
	}
	if (spfa(st)) {
		cout << num[ed] << " " << w[ed] << endl;
	} else {
		cout << "impossible" << endl;
	}
	return 0;
}