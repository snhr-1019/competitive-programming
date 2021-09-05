import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int L = sc.nextInt();
        int Q = sc.nextInt();

        TreeSet<Integer> set = new TreeSet<>();
        set.add(0);
        set.add(L);

        for (int i = 0; i < Q; i++) {
            int c = sc.nextInt();
            int x = sc.nextInt();
            if (c == 1) {
                set.add(x);
            } else {
                System.out.println(set.higher(x) - set.lower(x));
            }
        }
    }
}
