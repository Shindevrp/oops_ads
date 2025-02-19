import java.util.Scanner;
public class Solution{
    public static void main(String[] args) {
        Scanner a=new Scanner(System.in);
        float x1=a.nextFloat();
        float y1=a.nextFloat();
        float x=(x1*x1)+(y1*y1);
        double y=Math.sqrt(x);
        System.out.format("%.1f",y);
    }
}