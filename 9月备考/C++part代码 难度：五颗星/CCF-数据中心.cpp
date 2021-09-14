// 201812-4 数据中心
#include <iostream>
#include <algorithm>
using namespace std;
const int MAXE = 100010;
const int MAXV = 50010;

struct edge {
	int v, u;
	int cost;
} E[MAXE];

bool cmp(edge a, edge b) {
	return a.cost < b.cost;
}

int n, m, root;
int father[MAXV];
int findFather(int x) {
	int a = x;
	while (x != father[x]) {
		x = father[x];
	}
	while (a != father[a]) {
		int z = a;
		a = father[a];
		father[z] = x;
	}
	return x;
}

int kruskal() {
	int ans = 0;
	int Num = 0;
	//并查集初始化
	for (int i = 1; i <= n; i++) {
		father[i] = i;
	}
	sort(E, E + m, cmp);
	for (int i = 0; i < m; i++) {
		int faU = findFather(E[i].u);
		int faV = findFather(E[i].v);
		if (faU != faV) {
			father[faV] = faU;
			ans = E[i].cost;
			Num += 1;
			if (Num == n - 1)
				break;
		}

	}
	return ans;
}

int main() {
	cin >> n; // n个顶点
	cin >> m; // m条边
	cin >> root;
	int v, u, t;
	for (int i = 0; i < m; i++) {
		cin >> E[i].u >> E[i].v >> E[i].cost;
	}
	int res = kruskal();
	cout << res << endl;
	return 0;
}