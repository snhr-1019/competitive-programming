import java.util.*;

class Main {

    public static void main(String[] args) {
        Main m = new Main();
        m.run();
    }

    private void run() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Integer> r = new ArrayList<>();
        List<Integer> b = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            String c = sc.next();

            if (c.equals("R")) {
                r.add(x);
            } else {
                b.add(x);
            }
        }

        Collections.sort(r);
        Collections.sort(b);

        r.forEach(s -> System.out.println(s));
        b.forEach(s -> System.out.println(s));
    }
}
