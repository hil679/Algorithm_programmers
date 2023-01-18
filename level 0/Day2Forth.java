import java.util.*;


class Day2Forth{
    public static void main(String[] args) {//java에서 main 항상 정적 => 정적 method만 호출 가능, 따라서 solution에도 static
        int[] arr = {1,2,3,4};
        System.out.println(solution(arr));//new int[]{1,2,3,4}도 가능, {1,2,3,4}는 모호해서 안 됨
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