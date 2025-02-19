import java.util.ArrayList;
import java.util.Scanner;

class Student{
    String name;
    int rollnum;
    int marks;

    public Student(String n, int rn, int m){
        this.name = n;
        this.rollnum = rn;
        this.marks = m;
    }

    public char getGrades(){
        if (this.marks>=90){
            return 'A';
        }else if (this.marks >= 80 && this.marks < 90){
            return 'B';
        }else if (this.marks >= 70 && this.marks < 80){
            return 'C';
        }else{
            return 'D';
        }
    }
    // Name: Ian, Roll Number: 401, Marks: 90, Grade: A
    public String toString(){
        return "Name: "+this.name + ", Roll Number: "+this.rollnum + ", Marks: "+this.marks + ", Grade: " +this.getGrades();
    }
}

class GradeBook{
    ArrayList<Student> GB;

    public GradeBook(){
        GB = new ArrayList<Student>();
    }

    public void add_student(String name, int rn, int marks){
        Student s = new Student(name, rn, marks);
        GB.add(s);
    }

    public void display_students(){
        for (Student s : this.GB){
            System.out.println(s);
        }
    }

    public double calculate_average(){
        double total = 0;
        for (Student s: this.GB){
            total = total + s.marks;
        }
        return total/this.GB.size();
    }

}

public class Solution{
    public static void main(String[] args) {
        GradeBook gradebook = new GradeBook();
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextLine()){
            String[] input = sc.nextLine().split(" ");
            if (input.length == 5){
                String name = input[2].substring(0, input[2].length()-1);
                int rollnum = Integer.parseInt(input[3].substring(0, input[3].length()-1));
                int marks = Integer.parseInt(input[4]);
                gradebook.add_student(name, rollnum, marks);
            }else if (input[0].equals("DisplayStudents")){
                gradebook.display_students();
            }else if (input[0].equals("CalculateAverageMarks")){
                System.out.printf("Average Marks: %.2f\n",gradebook.calculate_average());
            }

        }
    }
}