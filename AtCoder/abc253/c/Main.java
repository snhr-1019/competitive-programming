import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int q = sc.nextInt();
        TreeMap<Integer, Integer> tm = new TreeMap<>();

        for (int i = 0; i < q; i++) {
            int query = sc.nextInt();

            if (query == 1) {
                int x = sc.nextInt();
                tm.put(x, tm.getOrDefault(x, 0) + 1);
            } else if (query == 2) {
                int x = sc.nextInt();
                int c = sc.nextInt();
                tm.put(x, tm.getOrDefault(x, 0) - c);
                if (tm.get(x) <= 0) {
                    tm.remove(x);
                }
            } else {
                System.out.println(tm.lastEntry().getKey() - tm.firstEntry().getKey());
            }
        }
    }
}
