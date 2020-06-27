import java.util.*;

import static java.lang.Math.*;

class Main {
    final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        new Main().run();
    }

    int n;
    int m;
    int k;
    int[] a;
    int[] b;

    private void run() {
        n = sc.nextInt();
        m = sc.nextInt();
        k = sc.nextInt();
        a = new int[n+1];
        b = new int[m+1];

        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        for (int i = 0; i < m; i++) {
            b[i] = sc.nextInt();
        }

        System.out.println(dp(0, 0, k));
    }

    /**
     * @param i Aの机の一番上がi番目
     * @param j Bの机の一番上がj番目
     * @return 読めた本の最大冊数
     */
    private long dp(int i, int j, int l) {
        if (i >= n || j >= m) {
            return -1;
        }

        // これ以上本を読めないときはそこまでの冊数を返す
        if (a[i] > l && b[j] > l) {
            return i + j;
        }

        long ans = max(dp(i + 1, j, l - a[i]), dp(i, j + 1, l - b[j]));
        return ans;
    }
}
