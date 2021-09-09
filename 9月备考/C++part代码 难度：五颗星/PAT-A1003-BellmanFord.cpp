//bellman ford�㷨  �����ڽӱ���ʽ�洢
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <cstring>
using namespace std;

struct Node {
	int v, dis; // v�����ڽӱߵ���һ�����㣬disΪ��Ȩ
	Node(int _v, int _dis) {
		v = _v;
		dis = _dis;
	}//���캯��
};
const int MAXV = 510; //��󶥵���
const int INF = 0x3fffffff;
vector<Node> Adj[MAXV]; //�ڽӱ�

int d[MAXV];//Դ�㵽��i����̾���
int w[MAXV], num[MAXV]; //w��¼·���ϵĵ�Ȩ   num��¼���·��������
int weight[MAXV];//��¼��Ȩ
int n, m, st, ed; //n������ m����
set<int> pre[MAXV];//��¼V�������ǰ��������ΪʲôҪ��set����

void BellmanFord(int st) { //stΪԴ��
	//��ʼ��d,num,w
	fill(d, d + MAXV, INF);
	d[st] = 0;
	memset(num, 0, sizeof num);
	num[st] = 1;
	memset(w, 0, sizeof w);
	w[st] = weight[st];

	//��ⲿ��
	bool flag = true;
	for (int i = 0; i < n - 1 & flag; i++) { //ִ��n-1�ֲ���
		flag = false;
		for (int u = 0; u < n; u++) { //����ÿһ����
			for (int j = 0; j < Adj[u].size(); j++) {
				int v = Adj[u][j].v;
				int dis = Adj[u][j].dis;

				if (d[u] + dis < d[v]) { //��uΪ�н��ʱ��ʹd[v]��С
					d[v] = d[u] + dis;
					w[v] = w[u] + weight[v]; // u��v����һ��·���ˣ����v�ĵ�ȨҪ����u��
					num[v] = num[u];//�ɵ���u��·��������v ����Ϊ�ɵ���u��ʾҲ�ɵ���v��

					pre[v].clear();  //���֮ǰv��ǰ��
					pre[v].insert(u); // �޸�ǰ��Ϊu
					flag = true;

				} else if (d[u] + dis == d[v]) { //dһ�� ����Ȩ�Ƿ���Ҫ����
					if (w[u] + weight[v] > w[v]) {
						w[v] = w[u] + weight[v];  // ����v�ĵ�Ȩ
					}
					pre[v].insert(u); // ��u����v��ǰ��
					num[v] = 0;//����ͳ��v
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
	cin >> n >> m >> st >> ed; // st��� ed�յ�
	for (int i = 0; i < n; i++) {
		cin >> weight[i];
	}
	int a, b, wt;
	for (int i = 0; i < m; i++) {
		cin >> a >> b >> wt;
		Adj[a].push_back(Node(b, wt));
		Adj[b].push_back(Node(a, wt));
	}//�����ڽӾ���
	//����

	//���Խ���
	BellmanFord(st); // ִ��bellman ford�㷨 �������·��
	printf("%d %d\n", num[ed], w[ed]);
	return 0;
}