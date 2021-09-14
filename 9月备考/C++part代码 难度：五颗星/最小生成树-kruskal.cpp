//最小生成树
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

const int INF = 0x3fffffff;
const int MAXV = 110; //代表最多顶点数
const int MAXE = 10010; //代表最多边数
struct edge {
	int u, v;
	int dis;
} E[MAXE];

bool cmp(edge a, edge b) {
	return a.dis < b.dis;
}

int n, m;
int father[MAXV];//并查集数组

/*
	伪代码：
	a 暂存当前要查找的数据x
	不断回溯寻找到数据x的根节点，寻找完x存储的是根节点！

	再次从当前要查找的数据出发，把查找路上经过的点的父节点都变为根节点。
	z 暂存当前要查找的数据a
	不断回溯寻找上一层节点，并将其father设为根节点。
*/

int findFather(int x) {
	// 并查集查询函数
	int a = x;
	while (x != father[x]) {
		x = father[x];
	}
	//路径压缩

	while (a != father[a]) {
		int z = a;
		a = father[a];
		father[z] = x;
	}
	return x;
}


int kruskal() {
	int ans = 0;//记录存放最小生成树的边权之和
	int NumEdge = 0;//当前生成树的边数
	for (int i = 1; i <= n; i++) { // 并查集初始化 每条边都是独立的，因此他们的父节点都是自己
		father[i] = i;
	}
	// 边排序
	sort(E, E + m, cmp);

	for (int i = 0; i < m; i++) {
		int faU = findFather(E[i].u);
		int faV = findFather(E[i].v);
		if (faU != faV) {
			father[faU] = faV;//将两条边合并到一个集合中
			ans += E[i].dis;
			NumEdge += 1;
			if (NumEdge == n - 1)
				break;
		}
	}
	if (NumEdge != n - 1)
		return -1;//无法连通
	else
		return ans;//返回最小生成树边权之和
}


int main() {
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		cin >> E[i].u >> E[i].v >> E[i].dis;
	}

	int ans = kruskal();
	cout << ans << endl;
	return 0;
}

/*
算法伪代码：
将所有的边权按照从小到大的顺序排列；
for(从小到大枚举所有边){
	if(当前测试边的两个端点属于两个不同的连通块中){
		当该测试边加入最小生成树中；
		ans += 测试边边权；
		最小生成树中边数num_edge加一；
		当边数num_edge等于顶点数减一时结束循环；
	}
}

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