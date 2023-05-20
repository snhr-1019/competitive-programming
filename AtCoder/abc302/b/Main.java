import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int w = sc.nextInt();

        char[][] s = new char[h][w];
        for (int i = 0; i < h; i++) {
            s[i] = sc.next().toCharArray();
        }

        char[] T = "snuke".toCharArray();

        int[] di = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dj = {-1, 0, 1, -1, 1, -1, 0, 1};

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                for (int k = 0; k < 8; k++) {
                    boolean ok = true;

                    for (int l = 0; l < 5; l++) {
                        int ci = i + di[k] * l;
                        int cj = j + dj[k] * l;

                        if (ci < 0 || ci >= h || cj < 0 || cj >= w) {
                            ok = false;
                            break;
                        }
                        if (s[ci][cj] != T[l]) {
                            ok = false;
                            break;
                        }
                    }

                    if (ok) {
                        for (int l = 0; l < 5; l++) {
                            int ci = i + di[k] * l;
                            int cj = j + dj[k] * l;

                            System.out.println((ci + 1) + " " + (cj + 1));
                        }
                    }
                }
            }
        }
    }
}
