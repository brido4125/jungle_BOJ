package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ12891 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int S = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(bf.readLine());
        String dna = st.nextToken();
        char[] dnaAry = dna.toCharArray();
        st = new StringTokenizer(bf.readLine());
        int[] min_number = new int[4];
        for (int i = 0; i < min_number.length; i++) {
            min_number[i] = Integer.parseInt(st.nextToken());
        }
        /* window의 시작 index */
        int start = 0;
        int end = P - 1;
        int answer = 0;
        int[] checkDNA = new int[4];
        setFirstWindow(dnaAry, start, end, checkDNA);
        boolean flag = isFlag(min_number, checkDNA);
        if (flag) {
            answer++;
        }
        while (end < S-1) {
            end++;
            addACGT(dnaAry,checkDNA,end);
            removeACGT(dnaAry, checkDNA, start);
            start++;
            flag = isFlag(min_number, checkDNA);
            if (flag) {
                answer++;
            }
        }
        System.out.println(answer);
    }

    private static boolean isFlag(int[] min_number, int[] checkDNA) {
        boolean flag = true;
        for (int i = 0; i < checkDNA.length; i++) {
            if(checkDNA[i] < min_number[i]) {
                flag = false;
            }
        }
        return flag;
    }

    private static void setFirstWindow(char[] dnaAry, int start, int end, int[] checkDNA) {
        for (int i = start; i <= end; i++) {
            addACGT(dnaAry, checkDNA, i);
        }
    }

    private static void addACGT(char[] dnaAry, int[] checkDNA, int i) {
        switch (dnaAry[i]) {
            case 'A':
                checkDNA[0]++;
                break;
            case 'C':
                checkDNA[1]++;
                break;
            case 'G':
                checkDNA[2]++;
                break;
            case 'T':
                checkDNA[3]++;
                break;
        }
    }

    private static void removeACGT(char[] dnaAry, int[] checkDNA, int i) {
        switch (dnaAry[i]) {
            case 'A':
                checkDNA[0]--;
                break;
            case 'C':
                checkDNA[1]--;
                break;
            case 'G':
                checkDNA[2]--;
                break;
            case 'T':
                checkDNA[3]--;
                break;
        }
    }
}
