import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner();
        int L = sc.nextInt();
        int Q = sc.nextInt();

        Set<Integer> set = new TreeSet<>();
        set.add(0);
        set.add(L);

        for (int i = 0; i < Q; i++) {
            int c = sc.nextInt();
            int x = sc.nextInt();
            if (c == 1) {
                set.add(x);
            } else {
                Object[] arr = set.toArray();
                int pos = Arrays.binarySearch(arr, x);
                System.out.print(Integer.getInteger(arr[pos].toString()) - Integer.getInteger(arr[pos - 1].toString()));
            }
        }
    }
}
