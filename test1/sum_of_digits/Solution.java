import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        long sum=DifferenceBetween(n);
        // System.out.println(sum);
        long diff = resultsum(sum);

        System.out.println(diff);
    }

    public static long DifferenceBetween(long n)
    
    {
    { 
        long sum = 0;
        while ( n !=0) {
            long l=n%10;

            sum += l;
            n/=10;
        }
        return sum;
    }
}
        
    public static long resultsum(long sum){
        long finalresult = 0;
        long temp=sum;
        // for (int i=0;i<=sum;i++)
        while(temp!=0)
        {
        long reminder=temp%10;
        finalresult+=reminder;
        temp/=10;
        
    }
        return finalresult;
        

    }
        
   
        
}




