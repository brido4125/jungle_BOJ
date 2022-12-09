package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ1253 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(bf.readLine());
        int[] ary = new int[N];
        for (int i = 0; i < N; i++) {
            ary[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(ary);
        int target = 0;
        int answer = 0;
        while (target != N) {
            int start = 0;
            int end = N-1;
            /* index가 다르면 서로 같은 값이라도 다른 수로 취급해야함 */
            while(start < end){
                if (ary[start] + ary[end] == ary[target]) {
                    if(start != target && end != target){
                        answer++;
                        break;
                    }
                    if(start == target){
                        start++;
                    }
                    else{
                        end--;
                    }
                } else if (ary[start] + ary[end] < ary[target]) {
                    start++;
                } else{
                    end--;
                }

            }
            target++;
        }
        System.out.println(answer);
    }
}
