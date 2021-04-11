import java.util.*;

import static java.lang.Math.*;

class Main {
    final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        new Main().run();
    }

    private void run() {
        long a = sc.nextLong();
        long r = sc.nextLong();
        long n = sc.nextLong();

        if (a > pow(10, 9) / pow(r, n - 1)) {
            System.out.println("large");
        } else {
            System.out.println((int) (a * pow(r, n - 1)));
        }
    }
}

