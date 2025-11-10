import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        StringBuilder sb = new StringBuilder();
        
        for(int i = 0; i < a.length(); i++){
            char k = a.charAt(i);
            
            if(Character.isUpperCase(k)){
                sb.append(Character.toLowerCase(k));
            }else{
                sb.append(Character.toUpperCase(k));
            }
        }
        System.out.println(sb.toString());
        
    }
}