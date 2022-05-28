import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int q = sc.nextInt();
        TreeSet<Integer> ts = new TreeSet<>();
        int[] cnt = new int[200010];

        for (int i = 0; i < q; i++) {
            int query = sc.nextInt();

            if (query == 1) {
                int x = sc.nextInt();
                ts.add(x);
            } else if (query == 2) {
                int x = sc.nextInt();
                int c = sc.nextInt();
                cnt[x] -= c;
                if (cnt[x] <= 0) {
                    cnt[x] = 0;
                    if (ts.contains(x)) {
                        ts.remove(x);
                    }
                }
            } else {
                System.out.println(ts.last() - ts.first());
            }
        }
    }
}
