import java.util.Scanner;
public class Solution{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        boolean soil_dry=sc.nextBoolean();
        boolean not_raning=sc.nextBoolean();
        boolean day_time=sc.nextBoolean();
        int temperature=sc.nextInt();
        boolean x=Automated_Garden_Watering_System(soil_dry, not_raning, day_time, temperature);
        System.out.println(x?"True":"False");
        



        
        
        
    }
    public static boolean Automated_Garden_Watering_System(boolean soil_dry, boolean not_raning,boolean day_time,int temperature ) {
        return soil_dry && !not_raning && day_time && temperature >10;        
    
    }

}