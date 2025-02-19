import java.nio.file.FileAlreadyExistsException;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        boolean a=calFactorial(n);
        System.out.println(a? "True": "False");

    }
    public static boolean calFactorial(int n){
        if ( n<=1){
            return false;

        }
        {
            for (int i=2;i<n;i++){
                if(n%i==0){
                    return false;
                }

            }
            return true;

        }
        
    }
}