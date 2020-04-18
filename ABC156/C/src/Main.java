import java.util.*;
import java.util.stream.Stream;

class Main {
    final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        new Main().run();
    }

    private void run() {
        int n = sc.nextInt();
        int l = Integer.MAX_VALUE;
        int r = Integer.MIN_VALUE;
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(sc.nextInt());
            l = Math.min(l, list.get(i));
            r = Math.max(r, list.get(i));
        }

        int minCost = Integer.MAX_VALUE;
        for (int p = l; p <= r; p++) {
            int cost = calc(p, list);
            if (cost < minCost) {
                minCost = cost;
            }
        }
        System.out.println(minCost);
    }

    private int calc(int p, List<Integer> list) {
        int cost = 0;
        list.stream().reduce((sum, i) -> { sum + i }).get();
        for (int j = 0; j < x.length; j++) {
            cost += Math.pow(x[j] - p, 2);
        }
        return cost;
    }
}
