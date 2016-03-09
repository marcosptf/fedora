/*


    "The singleton pattern is a design pattern that restricts the instantiation of a class to one object. This is useful when exactly one object is needed to coordinate actions across the system."
    - Wikipedia: Singleton Pattern

Complete the Singleton class in your editor which contains the following components:

    A private Singleton non parameterized constructor.
    A public String instance variable named strstr.
    Write a static method named getSingleInstance that returns the single instance of the Singleton class.

Once submitted, our hidden Solution class will check your code by taking a String as input and then using your Singleton class to print a line.

Input Format

You will not be handling any input in this challenge.

Output Format

You will not be producing any output in this challenge.

Sample Input

hello world

Sample Output

Hello I am a singleton! Let me say hello world to you


*/


import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.reflect.*;

 class Singleton{

    private static volatile Singleton st; 
    String str="Hello I am a singleton! Let me say hello world to you";
    
    public static Singleton getSingleInstance(){
        st = new Singleton();
        return st;
    }
   
    public Singleton(){
        Scanner sc=new Scanner(System.in);
        
        if(sc.hasNext()) {
            System.out.println(str);
        }
   } 

 }
