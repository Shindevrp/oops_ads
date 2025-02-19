import java.util.Scanner;
class Solution{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        boolean door_open = sc.nextBoolean();
        boolean window_open = sc.nextBoolean();
        boolean motion_detected = sc.nextBoolean();
        boolean alarm_deactivated = sc.nextBoolean();
        boolean a=Smart_Energy_home_System(door_open, window_open, motion_detected, alarm_deactivated);
        System.out.println(a? "True": "False");
    }
    public static boolean  Smart_Energy_home_System(boolean door_open, boolean  window_open , boolean motion_detected, boolean alarm_deactivated){
        return (door_open &&  ! alarm_deactivated) || ( window_open && !alarm_deactivated) ||
        ( motion_detected && !alarm_deactivated);
    }
}