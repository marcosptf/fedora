import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        int i;
        String s;
        Double d;
        Scanner scan = new Scanner(System.in);

        i = scan.nextInt();
        d = scan.nextDouble();
        s = scan.next() + " ";

        while(scan.hasNext()) {
            s += scan.next() + " ";
        }
        
        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}

