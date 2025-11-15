import java.util.*;

class Solution {
    public int solution(String dirs) {
        
        
        String[] list = dirs.split("");
        
        int[] location = {0,0};
        int cnt = 0;
        
        int[][] arr2 = new int[list.length][4];
        
        for(int i = 0; i < arr2.length; i++){
            arr2[i][0] = -6;
            arr2[i][1] = -6;
            arr2[i][2] = -6;
            arr2[i][3] = -6;
        }
        
        for(int i = 0; i < list.length; i++){
            int x1 = location[0];
            int y1 = location[1];
            int x2 = x1;
            int y2 = y1;
            
            if(list[i].equals("U")){
                y2 = y1 + 1;
            }else if(list[i].equals("D")){
                y2 = y1 - 1;
            }else if (list[i].equals("R")){
                x2 = x1 + 1;
            }else if(list[i].equals("L")){
                x2 = x1 - 1;
            }
            
            // 범위 체크
            if(x2 > 5 || x2 < -5 || y2 > 5 || y2 < -5){
                continue;
            }
            
            int visited = 0;
            for(int j = 0; j < arr2.length; j++){
                if(
                    (arr2[j][0] == x1 && arr2[j][1] == y1 && arr2[j][2] == x2 && arr2[j][3] == y2) || (arr2[j][0] == x2 && arr2[j][1] == y2 && arr2[j][2] == x1 && arr2[j][3] == y1)
                ){
                    visited = 1;
                    break;
                }
            }
            
            location[0] = x2;
            location[1] = y2;
            
            if(visited == 0){
                cnt++;
                arr2[i][0] = x1;
                arr2[i][1] = y1;
                arr2[i][2] = x2;
                arr2[i][3] = y2;
            }
        }
        return cnt;
    }
}