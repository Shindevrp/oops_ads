import java.util.Scanner;
public class  Solution{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x =sc.nextInt();
        int y =sc.nextInt();
        
        boolean a=diff_sum(x,y);
        System.out.println(a? "True":"False");


    }
    public static boolean diff_sum(int x, int y) {
        int diff=x-y;

        int sum1=x+y;

        if (diff ==5 || diff == -5 || sum1==5 || sum1== -5) {
            return true;
        } 
        else if (diff >5 || sum1>5) 
        {
            return false;
        }
         else if (diff <5 || sum1<5) {
            return false;
        }
        return false;


    } 
}

