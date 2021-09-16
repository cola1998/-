#include <iostream>
#include <cstring>

using namespace std;

const int N = 55;





char g[N][N];//�����ͼ
int r, c; //����������
//int dy[] = {1, 0, -1, 0},dx[] = {0, -1, 0, 1};
int dy[] = {0, 1, 0, -1};

int dx[] = {-1, 0, 1, 0};






bool st1[N][N] = {false}, st2[N][N] = {false};

bool check(int x, int y, int k) { //�ж�(x,y)�ܷ񵽴�k���� 0123��������
	if (g[x][y] == 'T' || g[x][y] == '+' || g[x][y] == 'S')
		return true;
	if (g[x][y] == '.' && k == 2)
		return true;
	if (g[x][y] == '|' && (k == 0 || k == 2))
		return true;
	if (g[x][y] == '-' && (k == 1 || k == 3))
		return true;
	return false;
}

void dfs1(int x, int y) {
	st1[x][y] = true;
	for (int i = 0; i < 4; i++) {
		int a = x + dx[i];
		int b = y + dy[i];
		if (check(x, y, i) && st1[a][b] == false && g[a][b] != '#') {
			//�����ǰλ��i����ɴ����û���߹���Ҳ����'#'
			dfs1(a, b);
		}
	}
}

void dfs2(int x, int y) {
	st2[x][y] = true;
	for (int i = 0; i < 4; i++) {
		int a = x + dx[i];
		int b = y + dy[i];
		int k = i ^ 2; //��λ���  ��ȥ�ķ��������ķ��� 0-2 1-3 2-0 3-1
		if (check(a, b, k) && st2[a][b] == false) {
			dfs2(a, b);
		}

	}
}

int main() {
	cin >> r >> c;
	int s_x, s_y, t_x, t_y;
	memset(g, '#', sizeof g);

	for (int i = 1; i <= r; i++) {
		for (int j = 1; j <= c; j++) {
			cin >> g[i][j];
			if (g[i][j] == 'S') {
				//�ҵ����
				s_x = i;
				s_y = j;
			}
			if (g[i][j] == 'T') {
				//�ҵ�Ŀ���
				t_x = i;
				t_y = j;
			}
		}
	}
	dfs1(s_x, s_y); // ���S���ߵ������е�
	for (int i = 1; i <= r; i++) {
		for (int j = 1; j <= c; j++) {
			cout << st1[i][j] << " ";
		}
		cout << endl;
	}
	if (st1[t_x][t_y] == false) {
		cout << "I'm stuck!" << endl;
		return 0;
	}
	dfs2(t_x, t_y); //����ܵ���T������·��
	cout << endl;
	for (int i = 1; i <= r; i++) {
		for (int j = 1; j <= c; j++) {
			cout << st2[i][j] << " ";
		}
		cout << endl;
	}
	int res = 0;
	for (int i = 1; i <= r; i++) {
		for (int j = 1; j <= c; j++) {
			if (st1[i][j] && !st2[i][j]) {
				res += 1;//s�ܵ�g[i][j] ��g[i][j]���ܵ�T
			}
		}
	}
	cout << res;
	return 0;
}
/*
���S���ߵ������е㡣
�����Щ���в�����T�������I��m stuck!
�������T��������ߵ�T������·����
ʣ�µĵ����s�ɴ���ǲ��ܵ�t�ĵ㡣
����ʹ��DFS��BFS��
*/