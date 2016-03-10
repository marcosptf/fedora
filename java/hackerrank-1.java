/*
In most of the HackerRank challenges, you need to read input from stdin (standard input) and write your output in stdout (standard output).
One way to take input from stdin is to use the Scanner class and read in from System.in.
You can write your output to stdout by simply using the System.out.println(String) function.
In this problem, you need to read 3 integers from stdin and print them in stdout. 

+Simple input 
42
100
125

+Simple output
42
100
125
*/

import java.util.*;

public class Solution {

    public static void main(String[] args) {
      Scanner sc=new Scanner(System.in);
      int value = 0;
        
      while(sc.hasNextInt()) {
          value = sc.nextInt();
          System.out.println(value);
      }
    }
}
