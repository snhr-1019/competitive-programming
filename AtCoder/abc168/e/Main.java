import java.util.*;

class Main {
    final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        new Main().run();
    }

    int n;
    boolean[] iwashi;
    int[] a;
    int[] b;
    Boolean[][] dp;

    final int t = 1000000007;

    private void run() {
        n = sc.nextInt();
        a = new int[n+2];
        b = new int[n+2];
        dp = new Boolean[n+2][n+2];
        iwashi = new boolean[n+2];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
            b[i] = sc.nextInt();
        }

        long ans = next(0);
        System.out.println(ans);

    }

    private long next(int i) {
        if (i == n+1) {
            return 1L;
        }

        for (int j = 0; j < i; j++) {
            // 選択していないイワシは無視
            if (!iwashi[j]) continue;

            // 1組でも相性の悪い組み合わせが入っていたら続けない
            if (!isGood(j, i)) {
                return 0L;
            }
        }
        long ans = 0;
        iwashi[i+1] = false;
        ans += next(i+1);

        iwashi[i+1] = true;
        ans += next(i+1);

        return ans % t;
    }

    private boolean isGood(int i, int j) {
        if (dp[i][j] != null) {
            return dp[i][j];
        }

        int d = a[i]*a[j] + b[i]*b[j];
        dp[i][j] = (d == 0);
        return dp[i][j];
    }
}

