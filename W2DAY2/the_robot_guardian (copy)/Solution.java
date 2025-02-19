import java.util.Scanner;
class Solution{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int age = sc.nextInt();
        boolean has_id = sc.nextBoolean();
        boolean password = sc.nextBoolean();
        // int current = sc.nextInt();
        boolean a=robot(age, has_id,password);
        System.out.println(a? "True": "False");
    }
    public static boolean  robot(int age, boolean has_id,boolean password){
        return (age >=18 && has_id) ||password ;
    }
}