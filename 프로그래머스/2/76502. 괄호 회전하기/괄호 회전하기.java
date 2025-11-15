import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        
        String[] str = s.split("");
        
        Deque<String> queue = new ArrayDeque<>();
        
        for(int i = 0; i < str.length; i++){
            queue.add(str[i]);
        }
        
        int len = str.length;
        
        String result = "";
        
        
        
        
        
        // 왼쪽으로 s번 만큼 회전 시켜서 
        for(int i = 0; i < len; i++){
            
            boolean cnt = true;
            
            Deque<String> queue2 = new ArrayDeque<>(queue);
            // int cnt = 0;
            
            Deque<String> queue3 = new ArrayDeque<>();
            
            
            for(int j = 0; j < queue.size(); j++){
                if(queue2.peekFirst().equals("(")){
                    queue2.pollFirst();
                    queue3.add("a");
                }else if (queue2.peekFirst().equals("{")){
                    queue2.pollFirst();
                    queue3.add("b");
                }else if (queue2.peekFirst().equals("[")){
                    queue2.pollFirst();
                    queue3.add("c");
                }else if(queue2.peekFirst().equals("]")){
                    queue2.pollFirst();
                    if(!queue3.isEmpty() && queue3.peekLast().equals("c")){
                        queue3.removeLast();
                    }else{
                        cnt = false;
                        break;
                    }
                }else if(queue2.peekFirst().equals("}")){
                    queue2.pollFirst();
                    if(!queue3.isEmpty() && queue3.peekLast().equals("b")){
                        queue3.removeLast();
                    }else{
                        cnt = false;
                        break;
                    }
                }else{
                    queue2.pollFirst();
                    if(!queue3.isEmpty() && queue3.peekLast().equals("a")){
                        queue3.removeLast();
                    }else{
                        cnt = false;
                        break;
                    }
                }
            }
            String x = queue.pollFirst();
            queue.add(x);
            
            if(queue3.size() > 0){
                cnt = false;
            }
            
            if(cnt == true){
                answer +=1;
            }
        }
        
        return answer;
    }
}