import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner a = new Scanner(System.in);
        String x = a.nextLine();

        System.out.println(time_conversion(x));            
    }
    
    public static String time_conversion(String x) {
        if (x.endsWith("PM")) {
            int hour = Integer.parseInt(x.substring(0, 2));
            
            if (hour < 12) {
                hour += 12;
            }
            return String.format("%02d", hour) + x.substring(2, x.length() - 2);
        } 
    
        else {
            int hour = Integer.parseInt(x.substring(0, 2));
            if (hour == 12) {
                hour = 0;
            }
            return String.format("%02d", hour) + x.substring(2, x.length() - 2);
        }
    }
}
