import javax.xml.transform.sax.SAXSource;
import java.util.*;

class Main {
    final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        new Main().run();
    }

    private void run() {
        int n = sc.nextInt();
        int before = sc.nextInt();
        for (int i = 1; i < n; i++) {
            int after = sc.nextInt();

            if (before == after) {
                System.out.println("stay");
            } else if (before > after) {
                System.out.printf("down %d\n", before - after);
            } else if (before < after) {
                System.out.printf("up %d\n", after - before);
            }
            before = after;
        }
    }
}

