//��С������
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

const int INF = 0x3fffffff;
const int MAXV = 110; //������ඥ����
const int MAXE = 10010; //����������
struct edge {
	int u, v;
	int dis;
} E[MAXE];

bool cmp(edge a, edge b) {
	return a.dis < b.dis;
}

int n, m;
int father[MAXV];//���鼯����

/*
	α���룺
	a �ݴ浱ǰҪ���ҵ�����x
	���ϻ���Ѱ�ҵ�����x�ĸ��ڵ㣬Ѱ����x�洢���Ǹ��ڵ㣡

	�ٴδӵ�ǰҪ���ҵ����ݳ������Ѳ���·�Ͼ����ĵ�ĸ��ڵ㶼��Ϊ���ڵ㡣
	z �ݴ浱ǰҪ���ҵ�����a
	���ϻ���Ѱ����һ��ڵ㣬������father��Ϊ���ڵ㡣
*/

int findFather(int x) {
	// ���鼯��ѯ����
	int a = x;
	while (x != father[x]) {
		x = father[x];
	}
	//·��ѹ��

	while (a != father[a]) {
		int z = a;
		a = father[a];
		father[z] = x;
	}
	return x;
}


int kruskal() {
	int ans = 0;//��¼�����С�������ı�Ȩ֮��
	int NumEdge = 0;//��ǰ�������ı���
	for (int i = 1; i <= n; i++) { // ���鼯��ʼ�� ÿ���߶��Ƕ����ģ�������ǵĸ��ڵ㶼���Լ�
		father[i] = i;
	}
	// ������
	sort(E, E + m, cmp);

	for (int i = 0; i < m; i++) {
		int faU = findFather(E[i].u);
		int faV = findFather(E[i].v);
		if (faU != faV) {
			father[faU] = faV;//�������ߺϲ���һ��������
			ans += E[i].dis;
			NumEdge += 1;
			if (NumEdge == n - 1)
				break;
		}
	}
	if (NumEdge != n - 1)
		return -1;//�޷���ͨ
	else
		return ans;//������С��������Ȩ֮��
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
�㷨α���룺
�����еı�Ȩ���մ�С�����˳�����У�
for(��С����ö�����б�){
	if(��ǰ���Աߵ������˵�����������ͬ����ͨ����){
		���ò��Ա߼�����С�������У�
		ans += ���Ա߱�Ȩ��
		��С�������б���num_edge��һ��
		������num_edge���ڶ�������һʱ����ѭ����
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
�����15
*/