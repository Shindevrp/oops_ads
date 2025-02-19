import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long diff = DifferenceBetween(n);
        System.out.println(diff);
    }

    public static long DifferenceBetween(int n) { 
        long Squares = 0;
        long sum = 0;

        for (int i = 1; i <= n; i++) {
            sum += i; 
            Squares += (long) i * i; 
        }

        long squareOfSum = sum * sum; 

        
        return squareOfSum - Squares;
    }
}
