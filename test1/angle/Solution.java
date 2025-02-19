import java.util.Scanner;
class Solution{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int angle=sc.nextInt();
        classify_angles(angle);

    }
    public static void classify_angles(int angle){
        if (0<angle  && angle<90){
            System.out.println("Acute");
        }
        else if(angle==90){
            System.out.println("Right");

        }
        else if(90 < angle && angle< 180){
            System.out.println("Obtuse");

        }
        else{
            System.out.println("Invalid");
        }
    
    }
}
