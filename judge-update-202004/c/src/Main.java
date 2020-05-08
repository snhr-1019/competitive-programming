import java.util.*;

class Main {
    int a1;
    int a2;
    int a3;
    int count;

    public static void main(String[] args) {
        Main m = new Main();
        m.run();
    }

    private void run() {
        Scanner sc = new Scanner(System.in);
        a1 = sc.nextInt();
        a2 = sc.nextInt();
        a3 = sc.nextInt();

        dfs(0,0, 0);
        System.out.println(count);
    }

    private void dfs(int x, int y, int z) {
        if (a1 > x) dfs(x+1, y, z);
        if (x > y && a2 > y) dfs(x, y+1, z);
        if (y > z && a3 > z) dfs(x, y, z+1);
        if (a1 == x && a2 == y && a3 == z) count++;
    }
}
