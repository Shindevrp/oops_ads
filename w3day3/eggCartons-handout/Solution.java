import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        egg(n);
    }

    public static void egg(int n) {
        if (n <= 0) {
            System.out.println(0);
            return;
        }

        
        int c = n / 12; 
        if (n % 12 != 0) {
            c += 1; 
        }
        

        System.out.println(c);
    }
}
