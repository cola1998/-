//spfa  ��Դ���·�����㷨
/*
n���� m��������ͼ �ұ�Ȩ����Ϊ��
��1-n����̾���
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
int n, m, st, ed; // n�����㣬m���ߣ�st��㣬ed�յ�
int d[MAXV], weight[MAXV]; //dis�����¼Դ�㵽��i����̾��� weight��¼��Ȩ
int num[MAXV], w[MAXV]; //num�����¼���·��������w��¼·��������Ȩ
int cnt[MAXV];//��¼Դ����Ӵ���
bool inq[MAXV];  //�����Ƿ��ڶ�����
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
		int u = Q.front(); //���ױ��Ϊu
		Q.pop();//����
		inq[u] = false;

		//����u�������ڽӱ�
		for (int j = 0; j < Adj[u].size(); j++) {
			int v = Adj[u][j].v;
			int dis = Adj[u][j].dis;

			//�ɳڲ���
			if (d[u] + dis < d[v]) {
				d[v] = d[u] + dis;
				w[v] = w[u] + weight[v];
				pre[v].clear();
				pre[v].insert(u);
				num[v] = num[u];
				if (!inq[v]) { //���v���ڶ����������������
					Q.push(v);
					inq[v] = true;
					cnt[v]++;  //v����Ӵ�����1
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
				if (!inq[v]) { //����w[v]�Ƿ�ı䣬num[v]�����ܸı䣬����Ҫ��ӣ�����
					Q.push(v);
					inq[v] = true;
					cnt[v]++;  //v����Ӵ�����1
				}
			}
			if (cnt[v] >= n)
				return false; //v����Ӵ�������n-1��˵�����ܴ��ڸ���
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