import java.util.*;

class Main {
    final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        new Main().run();
    }

    private void run() {
        String s = sc.next();
        String t = sc.next();
        if (s.equals(t)) {
            System.out.println("same");
        } else if (s.equalsIgnoreCase(t)) {
            System.out.println("case-insensitive");
        } else {
            System.out.println("different");
        }
    }
}

