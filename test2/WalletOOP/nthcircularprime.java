import java.util.Scanner;

class CircularPrime {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        System.out.println(findCircularPrime(number));            
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

    public static int countDigits(int num) {
        return String.valueOf(num).length();  
    }

    public static int[] getRotations(int num) {
        int size = countDigits(num);
        int[] rotations = new int[size];
        int power = (int) Math.pow(10, size - 1);

        for (int i = 0; i < size; i++) {
            rotations[i] = num;
            int lastDigit = num % 10;
            num = (num / 10) + (lastDigit * power);
        }
        return rotations;
    }

    public static boolean isCircularPrime(int num) {
        int[] rotations = getRotations(num);
        for (int rotatedNum : rotations) {
            if (!isPrime(rotatedNum)) {
                return false;
            }
        }
        return true;
    }

    public static int findCircularPrime(int count) {
        int found = 0, current = 2;

        while (true) {
            if (isCircularPrime(current)) {
                found++;
                if (found == count) {
                    return current;
                }
            }
            current++;
        }
    }
}
