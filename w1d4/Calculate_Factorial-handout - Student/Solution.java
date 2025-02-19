import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int result=calFactorial(n);
        System.out.println(result);

    }
    public static int calFactorial(int n){
        int res=1;
        for (int i=2; i<=n;i++){
        res*=i;
        }
        return res;
        
    }
}