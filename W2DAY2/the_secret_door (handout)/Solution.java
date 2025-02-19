import java.util.Scanner;
class Solution{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        boolean a1 = sc.nextBoolean();
        boolean b2 = sc.nextBoolean();
        boolean b3 = sc.nextBoolean();
        // int current = sc.nextInt();
        boolean a=Door(a1, b2, b3);
        System.out.println(a? "True": "False");
    }
    public static boolean  Door(boolean a1, boolean  b2, boolean b3){
        return (a1 && b2 && b3) || (a1 && b3 && !b2) || (b2 && (a1 || b3));
    }
}