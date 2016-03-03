/*
Congratulations, you passed this test case!

Input (stdin)

java 100
cpp 65
python 50

Your Output (stdout)

================================
java           100
cpp            065
python         050
================================

Expected Output

================================
java           100 
cpp            065 
python         050 
================================


*/

import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            String s, content, content2,  space = "";
            Integer contentInt = 16;
        
            System.out.println("================================");
            for(int i = 0 ;i < 3; i++){
                space = "";
                content = sc.next();
                content2 = sc.next();
                                    
                if (content2.length() < 3){
                    content2 = "0" + content2;
                }
                
                for (int x = 1; x < (contentInt - content.length()); x++){
                    space += " ";
                }
                
                System.out.println(content + space + content2);
            }
            System.out.println("================================");

    }
}
