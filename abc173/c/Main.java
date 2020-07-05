import java.util.*;
import static java.lang.Math.*;

class Main {
    final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        new Main().run();
    }

    int h;
    int w;
    int k;
    String[][] grid;
    int[] cntH;
    int[] cntW;
    int cnt;
    private void run() {
        h = sc.nextInt();
        w = sc.nextInt();
        k = sc.nextInt();
        grid = new String[h][w];
        cnt = 0;
        cntH = new int[h];
        cntW = new int[w];

        for (int i = 0; i < h; i++) {
            grid[i] = sc.next().split("");
            for (int j = 0; j < w; j++) {
                if (grid[i][j].equals("#")) {
                    cntH[i]++;
                    cnt++;
                }
            }
        }

        for (int i = 0; i < w; i++) {
            for (int j = 0; j < h; j++) {
                if (grid[j][i].equals("#")) {
                    cntW[i]++;
                }
            }
        }

        // 全探索
        for (int i = 0; i < 1 << h; i++) {
            for (int l = 0; l < 1 << w; l++) {
                int tmpCnt = cnt;
                for (int j = 0; j < h; j++) {
                    if ((1 & i >> j) == 1) {
                        tmpCnt -= cntW[j];
                    }
                }
            }
        }
    }
}
