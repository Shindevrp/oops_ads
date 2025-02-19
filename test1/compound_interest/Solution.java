import java.util.Scanner;
import java.lang.Math;
class Solution{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int p=sc.nextInt();
        float r=sc.nextFloat();
        int t=sc.nextInt();
        // double result =interest(p,r,t)
        // System.out.format("%.2f" , result);
        interest(p, r, t);
    }
    public static void interest(int p,float r,int t){
        double Amount = p *( Math.pow((1 + r/ 100), t));
        double CI = Amount - p;
        System.out.format("%.2f" , CI);

    }
}