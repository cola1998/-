#include <iostream>
#include <cstring>
#include <utility>
using namespace std;
const int N = 55;
int n, m;
bool st1[N][N], st2[N][N]; //记录是否可达
char g[N][N];

int dx[] = {-1, 0, 1, 0};

int dy[] = {0, -1, 0, 1};

bool check(int x, int y, int k) {
	if (g[x][y] == 'S' || g[x][y] == 'T' || g[x][y] == '+') {
		return true;
	}
	if (g[x][y] == '.' && k == 2)
		return true;
	if (g[x][y] == '|' && (k == 0 || k == 2))
		return true;
	if (g[x][y] == '-' && (k == 1 || k == 3))
		return true;
	return false;
}

void bfs1(int x, int y) {
	st1[x][y] = true;
	pair<int, int> q[N];
	q[0] = {x, y};
	int t = 0, h = 0;
	while (h <= t) {
		int x0 = q[h].first, y0 = q[h].second;
		st1[x0][y0] = true;
		for (int i = 0; i < 4; i++) {
			int a = x0 + dx[i], b = y0 + dy[i];
			if (check(x0, y0, i) && st1[a][b] == false && g[a][b] != '#') {
				q[t++] = {a, b};
			}
		}
		h += 1;
	}
}

void bfs2(int x, int y) {
	st2[x][y] = true;
	pair<int, int> q[N];
	q[0] = {x, y};
	int t = 0, h = 0;
	while (h <= t) {
		int x0 = q[h].first, y0 = q[h].second;
		st2[x0][y0] = true;
		for (int i = 0; i < 4; i++) {
			int k = i ^ 2;
			int a = x0 + dx[i], b = y0 + dy[i];
			if (check(a, b, k) && st2[a][b] == false ) {
				q[t++] = {a, b};
			}
		}
		h += 1;
	}
}

int main() {
	cin >> n >> m;
	int s_x, s_y, t_x, t_y;
	memset(g, '#', sizeof g);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			cin >> g[i][j];
			if (g[i][j] == 'S') {
				s_x = i;
				s_y = j;
			}
			if (g[i][j] == 'T') {
				t_x = i;
				t_y = j;
			}
		}
	}
	bfs1(s_x, s_y);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			cout << st1[i][j] << " ";
		}
		cout << endl;
	}
	if (st1[t_x][t_y] == false) {
		cout << "I'm stuck!" << endl;
		return 0;
	}
	bfs2(t_x, t_y);
	cout << endl;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			cout << st2[i][j] << " ";
		}
		cout << endl;
	}
	int res = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (st1[i][j] == true && st2[i][j] == false)
				res += 1;
		}
	}
	cout << res;
	return 0;
}