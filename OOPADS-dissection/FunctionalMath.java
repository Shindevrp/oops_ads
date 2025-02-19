import java.util.*;
import java.util.function.*;
import java.util.stream.*;

public class FunctionalMath {

    public static void main(String[] args) {
        // Example of Lambda Expression
        BiFunction<Integer, Integer, Integer> add = (x, y) -> x + y;
        System.out.println("Addition: " + add.apply(5, 3));

        // Functional Interface with Streams
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6);
        List<Integer> filtered = numbers.stream()
                                        .filter(x -> x % 2 == 0)
                                        .collect(Collectors.toList());
        System.out.println("Filtered Even Numbers: " + filtered);

        // Method Reference
        List<Double> squares = numbers.stream()
                                       .map(Math::sqrt)
                                       .collect(Collectors.toList());
        System.out.println("Square Roots: " + squares);

        // Higher-Order Function
        System.out.println("Custom Operation (Multiplication): " +
                applyOperation(6, 7, (a, b) -> a * b));

        // Recursion
        System.out.println("Factorial of 5: " + factorial(5));

        // Lazy Evaluation
        Stream<Double> randomNumbers = Stream.generate(Math::random).limit(5);
        randomNumbers.forEach(System.out::println);
    }

    public static int applyOperation(int x, int y, BiFunction<Integer, Integer, Integer> operation) {
        return operation.apply(x, y);
    }

    public static int factorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }
}
