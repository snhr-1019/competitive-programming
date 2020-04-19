import java.util.*;

class Main {
    final Scanner sc = new Scanner(System.in);

    final long DEVIDE = 1000000007;


    public static void main(String[] args) {
        new Main().run();
    }

    private void run() {
        List<Long> list = new ArrayList<>();
        long n = sc.nextLong();
        for (int i = 0; i <= n; i++) {
            long a = (long)(Math.pow(10,100)+i);
            long t = ((long)(Math.pow(10,100)+i) % DEVIDE);
            if (t < n) break;
            list.add(t);
        }
        System.out.println(list.toArray());
    }
}
