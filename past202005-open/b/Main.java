import java.util.*;

class Main {
    final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        new Main().run();
    }

    private void run() {
        int n = sc.nextInt();
        int m = sc.nextInt();
        int q = sc.nextInt();
        // 各問題の解けた人数
        int[] c = new int[m];
        // 各人の解けた問題
        boolean[][] d = new boolean[n][m];

        int n1;
        int m1;
        for (int i = 0; i < q; i++) {
            switch (sc.nextInt()) {
                case 1:
                    n1 = sc.nextInt()-1;
                    int ans = 0;
                    for (int j = 0; j < m; j++) {
                        if (d[n1][j]) {
                            ans += n - c[j];
                        }
                    }
                    System.out.println(ans);
                    break;
                case 2:
                    n1 = sc.nextInt()-1;
                    m1 = sc.nextInt()-1;
                    c[m1]++;
                    d[n1][m1] = true;
                    break;
            }
        }
    }
}

