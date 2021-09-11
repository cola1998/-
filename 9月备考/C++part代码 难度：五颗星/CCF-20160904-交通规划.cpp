//csp 201609-4  ��ͨ�滮
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
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
int n, m;
vector<Node> Adj[MAXV];
int d[MAXV];
bool inq[MAXV];  //���ڼ�¼�Ƿ��ڶ�����
//set<int> pre[MAXV];
int pre[MAXV];//���ڼ�¼ǰ���ڵ�
//int ans[MAXV];//�湹�����·���ı�

void spfa(int st) {
	fill(d, d + MAXV, INF);
	d[st] = 0;
	memset(inq, false, sizeof inq);
	queue<int> Q;
	Q.push(st);
	inq[st] = true;
	pre[st] = st;
	while (!Q.empty()) {
		int u = Q.front();
		Q.pop();
		inq[u] = false;
		//cout << "u=" << u << endl;
		for (int j = 0; j < Adj[u].size(); j++) {
			int v = Adj[u][j].v;
			int dis = Adj[u][j].dis;

			//cout << "v=" << v << endl;
			if (d[u] + dis < d[v]) {
				d[v] = d[u] + dis;
				pre[v] = u; //����pre
				//ans[v] = dis;
				if (!inq[v]) {
					Q.push(v);
					inq[v] = true;
				}
			} else if (d[u] + dis == d[v]) {
				//cout << "==" << d[pre[v]] << " " << d[u] << endl;
				if (d[pre[v]] < d[u]) { //�����·����ͬʱ�����d[u]����v֮ǰ��·�����ȲŸ��£���ʾu->v����С��
					pre[v] = u;
				}
			}
		}
	}
}

int main() {
	cin >> n >> m;
	int a, b, c;
	for (int i = 1; i <= m; i++) {
		cin >> a >> b >> c;
		Adj[a].push_back(Node(b, c));
		Adj[b].push_back(Node(a, c));
	}
//	for (int i = 1; i <= n; i++) {
//		cout << i << endl;
//		for (int j = 0; j < Adj[i].size(); j++) {
//			cout << Adj[i][j].v << " " << Adj[i][j].dis << endl;
//		}
//	}
	spfa(1);
	int res = 0;
//	for (int i = 1; i <= n; i++) {
//		cout << d[i] << endl;
//	}
	for (int i = 2; i <= n; i++) {
		res = res + d[i] - d[pre[i]];
		//cout << res << " " << pre[i] << " " << d[pre[i]] << endl;
	}
	cout << res << endl;
	return 0;
}