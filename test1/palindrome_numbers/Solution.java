import java.util.Scanner;
class Solution{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int n =sc.nextInt();

    }
    public static void finde(int n){
        int left = 0;
        int right = n.length() - 1;
        
    while (left <= right)
    {
        if (n.charAt(left) != n.charAt(right))
        {
            return false;
        }
        left++;
        right--;
    }
    return true;


    }
}