import java.util.*;

class Main {
    final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        new Main().run();
    }

    private void run() {
        String s = sc.next();
        if (!s.matches("[0-9]+")) {
            System.out.println("error");
            return;
        }
        System.out.println(Integer.parseInt(s) * 2);
    }
}

