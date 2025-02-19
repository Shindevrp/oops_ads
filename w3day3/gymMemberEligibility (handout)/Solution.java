import java.util.Scanner;
public class  Solution{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int age =sc.nextInt();
        double bmi=sc.nextDouble();
        boolean healthCondition=sc.nextBoolean();
        boolean a=gym(age,bmi,healthCondition);
        System.out.println(a? "True":"False");


    }
    public static boolean gym(int age, double bmi, boolean healthCondition){
        return (age >= 18 && age <= 60 && bmi >= 18.5 && bmi <= 24.9 && !healthCondition) ||
               (age < 18 && bmi >= 18.5 && bmi <= 24.9) ||
               (age > 60 && bmi >= 18.5 && bmi <= 24.9 && !healthCondition);
    }


    } 

