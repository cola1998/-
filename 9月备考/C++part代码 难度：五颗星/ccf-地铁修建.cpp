//csp 201703-4 �����޽� kruskal
#include <iostream>
#include <algorithm>

using namespace std;
const int MAXE = 200010;
const int MAXV = 100010;
struct edge {
	int u, v;
	int cost;
} E[MAXE];

bool cmp(edge a, edge b) {
	return a.cost < b.cost;
}
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
int n, m;

int krustral() {
	int MAX = 0;
	int NumEdge = 0;

	for (int i = 1; i <= n; i++) {
		father[i] = i; //���鼯��ʼ��
	}
	//������
	sort(E, E + m, cmp);
	for (int i = 0; i < m; i++) {
		int faU = findFather(E[i].u);
		int faV = findFather(E[i].v);
		if (faU != faV) {
			father[faV] = faU;
		}//�ϲ�
		MAX = E[i].cost;

		if (findFather(1) == findFather(n)) {
			//cout << "find! " << findFather(1) << " " << findFather(n) << endl;
			break;
		}
	}
	return MAX;
}

int main() {
	//������޽�1��n�ŵ� Ȼ��ѡ�񷽰�ʵʩ���������Ǹ�
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		cin >> E[i].u >> E[i].v >> E[i].cost;
	}
	int res = krustral();
	if (res != -1)
		cout << res << endl;
	else
		cout << "-1" << endl;
	return 0;
}