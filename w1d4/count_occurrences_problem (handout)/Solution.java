import java.util.Scanner;
public class Solution {

    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        String first= sc.nextLine();
        String second=sc.nextLine();
        int count=countOccurrences(first,second);
        System.out.println(count);
        
    }
    public static int countOccurrences(String first,String second){
        if (second.isEmpty()){
            return 0;
        }

        int c = 0;

        for (int i = 0; i <= first.length() - second.length(); i++) {
            if (first.substring(i, i + second.length()).equals(second)) {
                c++;
            }
        }

        return c;
    }

}