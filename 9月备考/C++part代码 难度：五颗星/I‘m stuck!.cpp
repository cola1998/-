#include <iostream>
#include <cstring>

using namespace std;

const int N = 55;





char g[N][N];//保存地图
int r, c; //行数和列数
//int dy[] = {1, 0, -1, 0},dx[] = {0, -1, 0, 1};
int dy[] = {0, 1, 0, -1};

int dx[] = {-1, 0, 1, 0};






bool st1[N][N] = {false}, st2[N][N] = {false};

bool check(int x, int y, int k) { //判断(x,y)能否到达k方向 0123上左下右
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
			//如果当前位置i方向可达，并且没有走过，也不是'#'
			dfs1(a, b);
		}
	}
}

void dfs2(int x, int y) {
	st2[x][y] = true;
	for (int i = 0; i < 4; i++) {
		int a = x + dx[i];
		int b = y + dy[i];
		int k = i ^ 2; //按位异或  回去的方向是来的反向 0-2 1-3 2-0 3-1
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
				//找到起点
				s_x = i;
				s_y = j;
			}
			if (g[i][j] == 'T') {
				//找到目标点
				t_x = i;
				t_y = j;
			}
		}
	}
	dfs1(s_x, s_y); // 求出S能走到的所有点
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
	dfs2(t_x, t_y); //求出能到达T的所有路线
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
				res += 1;//s能到g[i][j] 但g[i][j]不能到T
			}
		}
	}
	cout << res;
	return 0;
}
/*
求出S能走到的所有点。
如果这些点中不包含T，则输出I’m stuck!
如果包含T，求出能走到T的所有路径。
剩下的点就是s可达，但是不能到t的点。
可以使用DFS和BFS！
*/