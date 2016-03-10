/*
+Sample Input
42
3.1415
Welcome to HackerRank Java tutorials

+Sample Output
String: Welcome to HackerRank Java tutorials!
Double: 3.1415
Int: 42

============================ error ==================================
Nice try, but you did not pass this test case.

Input (stdin)

42
3.1415
Welcome to Hackerrank Java tutorials!

Your Output (stdout)

String: Welcome
Double: 3.1415
Int: 42

Expected Output

String: Welcome to Hackerrank Java tutorials!
Double: 3.1415
Int: 42

Compiler Message

Wrong Answer
=====================================================================
*/

import java.util.Scanner;
public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s, out1, out2, out3;
        Double d;
        Integer i;

        i = sc.nextInt();
        out3 = "Int: " + i.toString();    
        d = sc.nextDouble();
        out1 = "Double: " + d.toString();
        s = sc.next();
        out2 = "String: " + s.toString();
        
        System.out.println(out2);
        System.out.println(out1);
        System.out.println(out3);        
    }
}
