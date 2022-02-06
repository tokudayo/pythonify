public class Example {
    private static void permute(int n, char[] a) {
        if (n == 0) {
            System.out.println(String.valueOf(a));
        }
        else {
            for (int i = 0; i <=n; i++) {
                permute(n - 1, a);
                swap(a, n % 2 == 0 ? i : 0, n);
            }
        }
    }

    private static void swap(char[] a, int i, int j) {
        char saved = a[i];
        a[i] = a[j];
        a[j] = saved;
    }

    public static void main() {
        char[] a = "Hello world".toCharArray();
        permute(5, a);
    }
}