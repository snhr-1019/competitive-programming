import java.util.*;

class Main {
    final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        new Main().run();
    }

    long a;
    long b;
    long x;

    private void run() {
        a = sc.nextLong();
        b = sc.nextLong();
        x = sc.nextLong();

        long n = 1000000000;
        if (canBuy(n)) {
            System.out.println(n);
            return;
        }
        long left = 0;
        long right = n;
        long mid = 0;
        while (right - left > 1) {
            mid = (left + right) / 2;
            if (canBuy(mid)) {
                left = mid;
            } else {
                right = mid;
            }
        }
        System.out.println(left);
    }

    private boolean canBuy(long n) {
        return a * n + b * Long.toString(n).length() <= x;
    }
}

