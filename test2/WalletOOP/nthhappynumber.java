import java.util.Scanner;

class NoobHappyPrime {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        System.out.println(getHappyPrime(num));            
    }

    public static boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) { 
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static boolean isHappy(int num) {
        while (num != 1 && num != 4) { 
            int sum = 0;
            while (num > 0) {
                int digit = num % 10;
                sum += digit * digit;
                num /= 10;
            }
            num = sum;
        }
        return num == 1;
    }

    public static int getHappyPrime(int pos) {
        int count = 0, num = 7; 

        while (true) {
            if (isPrime(num) && isHappy(num)) {
                count++;
                if (count == pos) {
                    return num;
                }
            }
            num++;
        }
    }
}
