import java.util.Scanner;
public class  Solution{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int age =sc.nextInt();
        float annual_income=sc.nextFloat();
        int credit_score=sc.nextInt();
        float current_debts=sc.nextFloat();
        boolean a=loan(age,annual_income,credit_score,current_debts);
        System.out.println(a? "True":"False");


    }
    public static boolean loan(int age, float annual_income, int credit_score, float current_debts) {
        if (age >= 25 && age <= 65 && annual_income >= 50000 && credit_score >= 700 && current_debts < 50000) {
            return true;
        } 
        else if (age < 25 && annual_income >= 70000 && credit_score >= 750 && current_debts < 30000) 
        {
            return true;
        }
         else if (age > 65 && annual_income >= 40000 && credit_score >= 650 && current_debts < 20000) {
            return true;
        }
        return false;


    } 
}

