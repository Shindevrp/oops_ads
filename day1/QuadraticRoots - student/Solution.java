import java.util.Scanner;
public class Solution{
    public static void main(String[] args) {
        Scanner a=new Scanner(System.in);
        float x=a.nextFloat();
        float y= a.nextFloat();
        float z=(x*x)-(4*y);
        double z1=Math.sqrt(z);
        System.out.println((-x+z1)/2);
        System.out.println((-x-z1)/2);
    }
}