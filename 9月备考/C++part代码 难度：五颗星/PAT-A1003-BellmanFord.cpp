//bellman ford算法  采用邻接表形式存储
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <cstring>
using namespace std;

struct Node {
	int v, dis; // v代表邻接边的另一个顶点，dis为边权
	Node(int _v, int _dis) {
		v = _v;
		dis = _dis;
	}//构造函数
};
const int MAXV = 510; //最大顶点数
const int INF = 0x3fffffff;
vector<Node> Adj[MAXV]; //邻接表

int d[MAXV];//源点到点i的最短距离
int w[MAXV], num[MAXV]; //w记录路径上的点权   num记录最短路径条数？
int weight[MAXV];//记录点权
int n, m, st, ed; //n顶点数 m边数
set<int> pre[MAXV];//记录V个顶点的前驱？？？为什么要用set？？

void BellmanFord(int st) { //st为源点
	//初始化d,num,w
	fill(d, d + MAXV, INF);
	d[st] = 0;
	memset(num, 0, sizeof num);
	num[st] = 1;
	memset(w, 0, sizeof w);
	w[st] = weight[st];

	//求解部分
	bool flag = true;
	for (int i = 0; i < n - 1 & flag; i++) { //执行n-1轮操作
		flag = false;
		for (int u = 0; u < n; u++) { //遍历每一条边
			for (int j = 0; j < Adj[u].size(); j++) {
				int v = Adj[u][j].v;
				int dis = Adj[u][j].dis;

				if (d[u] + dis < d[v]) { //以u为中介点时能使d[v]变小
					d[v] = d[u] + dis;
					w[v] = w[u] + weight[v]; // u和v构成一条路径了，因此v的点权要加上u的
					num[v] = num[u];//可到达u的路径数赋给v ，因为可到达u表示也可到达v了

					pre[v].clear();  //清除之前v的前驱
					pre[v].insert(u); // 修改前驱为u
					flag = true;

				} else if (d[u] + dis == d[v]) { //d一样 检查点权是否需要更新
					if (w[u] + weight[v] > w[v]) {
						w[v] = w[u] + weight[v];  // 更新v的点权
					}
					pre[v].insert(u); // 将u加入v的前驱
					num[v] = 0;//重新统计v
					set<int>::iterator it;
					for (it = pre[v].begin(); it != pre[v].end(); it++) {
						num[v] += num[*it];
					}
					flag = true;
				}
			}
		}
	}
}

int main() {
	cin >> n >> m >> st >> ed; // st起点 ed终点
	for (int i = 0; i < n; i++) {
		cin >> weight[i];
	}
	int a, b, wt;
	for (int i = 0; i < m; i++) {
		cin >> a >> b >> wt;
		Adj[a].push_back(Node(b, wt));
		Adj[b].push_back(Node(a, wt));
	}//构建邻接矩阵
	//调试

	//调试结束
	BellmanFord(st); // 执行bellman ford算法 计算最短路径
	printf("%d %d\n", num[ed], w[ed]);
	return 0;
}