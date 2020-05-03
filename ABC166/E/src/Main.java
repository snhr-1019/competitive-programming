import java.util.*;

class Main {
    final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        new Main().run();
    }

    private void run() {
        int n = sc.nextInt();
        Map<Long, Long> add = new TreeMap<>();
        Map<Long, Long> sub = new TreeMap<>();
        long[] arr = new long[n+1];

        for (int i = 1; i <= n; i++) {
            long a = sc.nextLong();
            arr[i] = a;
            add.put(i+a, add.getOrDefault(i + a, 0L)+1);
            sub.put(i-a, sub.getOrDefault(i - a, 0L)+1);
        }

        int ans = 0;
        for(Map.Entry<Long, Long> addentry : add.entrySet()) {
            if (sub.containsKey(addentry.getKey())) {
                ans += addentry.getValue() * sub.get(addentry.getKey());
            }
        }
        System.out.println(ans);
    }
}
