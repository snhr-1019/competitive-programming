import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        var n = sc.nextInt();
        var k = sc.nextInt();
        var s = sc.next();

        var ans = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (k > 0 && s.charAt(i) == 'o') {
                k--;
                ans.append('o');
            } else {
                ans.append('x');
            }
        }
        System.out.println(ans);
    }
}
