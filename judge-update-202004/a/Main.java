import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int s = sc.nextInt();
        int l = sc.nextInt();
        int r = sc.nextInt();
        if (l <= s && s <= r) {
            System.out.println(s);
        } else if (s < l) {
            System.out.println(l);
        } else if (r < s) {
            System.out.println(r);
        }
    }
}
