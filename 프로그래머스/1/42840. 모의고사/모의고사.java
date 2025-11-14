import java.util.*;


class Solution {
    public int[] solution(int[] answers) {
        // 1번 수포자 => 1, 2, 3, 4, 5, 1
        // 2번 수포자 => 2, 1, 2, 3, 2, 4, 2, 5, 2, 1
        int[] answer = {};
        
        int[] num1 = new int[answers.length];
        int[] num2 = new int[answers.length];
        int[] num3 = new int[answers.length];
        int[] result = new int[3];
        
        // 3명의 수포자들의 배열 만들기
        // 1번 수포자
        for(int i = 0; i < answers.length; i++){
            if((i+1) % 5 == 1){
                num1[i] = 1;
            }else if((i+1) % 5 == 2){
                num1[i] = 2;
            }else if((i+1) % 5 == 3){
                num1[i] = 3;
            }else if((i+1) % 5 == 4){
                num1[i] = 4;
            }else{
                num1[i] = 5;
            }
        }
        
        // 2번 수포자
        for(int i = 0; i < answers.length; i++){
            if(i % 2 == 0){
                num2[i] = 2;
            }else{
                if((i+1) % 8 == 2){
                    num2[i] = 1;
                }
                else if((i+1) % 8 == 4){
                    num2[i] = 3;
                }else if((i+1) % 8 == 6){
                    num2[i] = 4;
                }else{
                    num2[i] = 5;
                }
            }
        }
        
        // 3번 수포자
        for(int i = 0; i < answers.length; i++){
            if((i+1) % 10 == 1 || (i+1) % 10 == 2){
                num3[i] = 3;
            }else if((i+1) % 10 == 3 || (i+1) % 10 == 4){
                num3[i] = 1;
            }else if((i+1) % 10 == 5 || (i+1) % 10 == 6){
                num3[i] = 2;
            }else if((i+1) % 10 == 7 || (i+1) % 10 == 8){
                num3[i] = 4;
            }else{
                num3[i] = 5;
            }
        }
        
        
        // 1. 인원수(i)만큼 반복하기
        for(int i = 0; i < 3; i++){
            int cnt = 0;
            // 2. 문제 갯수만큼 반복하기
            for(int j = 0; j < answers.length; j++){
                if(i == 0){
                    if (num1[j] == answers[j]){
                        cnt+=1;
                    }
                }else if(i == 1){
                    if (num2[j] == answers[j]){
                        cnt+=1;
                    }
                }else{
                    if (num3[j] == answers[j]){
                        cnt+=1;
                    }
                }
            }
            result[i] = cnt;
            
        }
        
        int maxNum = result[0];
        
        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(1);
        for(int i = 1; i < result.length; i++){
            
            
            if(result[i] >= maxNum){
                if(result[i] > maxNum){
                    arr.remove(0);
                }
                arr.add(i+1);
                maxNum = result[i];
            }
        }
        
        int[] total = arr.stream()
                        .mapToInt(Integer::intValue)
            .toArray();
        return total;
        
    }
}