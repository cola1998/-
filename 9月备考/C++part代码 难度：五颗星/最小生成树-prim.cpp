//��С������
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
int d[MAXV];//�洢����Vi�뼯��S����̾���  ��Χ�����Dijkstra�㷨��d��С��
//��Dijkstra��d�ĺ��������st������Vi����̾��롿
vector<Node> Adj[MAXV];

bool vis[MAXV];//�洢�����Ƿ񱻰ݷù�
int prim() {
	memset(vis, false, sizeof vis);
	fill(d, d + MAXV, INF);
	d[0] = 0;
	int ans = 0;//��¼�����С�������ı�Ȩ֮��
	for (int i = 0; i < n; i++) {
		int u = -1, MIN = INF; //Ѱ��d[u]��С��δ�����ʹ��ı��
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
		for (int j = 0; j < Adj[u].size(); j++) { //����������u�����Ķ���v
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
�㷨α���룺
��ʼ������vis��d
for(ѭ��n��):
	u = ʹd[u]��С�Ļ�δ�����ʹ��Ķ����ţ�
	��u�Ѿ������ʹ���
	for ��u�������Ե���Ķ���v:
		���vû�б����ʣ�����d[v]<d[u]+dis:
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
�����15
*/