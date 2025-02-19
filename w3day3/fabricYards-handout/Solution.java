import java.util.Scanner;



class Solution{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int inches = sc.nextInt();
        Fabric_yarn(inches);
        
    }

    public static void  Fabric_yarn(int inches){
        if (inches == 0){
            System.out.println(0);
        }else if(inches <= 36){
            System.out.println(1);
        }else{
            if (inches%36 == 0){
                System.out.println(inches/36);
            }else{
                System.out.println(inches/36 + 1);
            }
        }
    }
}