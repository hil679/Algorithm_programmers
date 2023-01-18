import java.util.*;


class Day2Forth{
    public static void main(String[] args) {
        System.out.println(solution(new int[]{1,2,3,4}));
    }
    public static int[] solution(int[] numbers) {
        int[] answer = {};
        ArrayList<Integer> ansList = new ArrayList<>();
        for (int n : numbers)
        {
            ansList.add(n * 2);
        }
        System.out.println(ansList);
        answer = ansList.stream()
                .mapToInt(i -> i)
                .toArray();
        return answer;
    }
    
}