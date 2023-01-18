import java.util.*;

class FindMode {
    public static void main(String[] args) {
        System.out.println(solution(new int[] {2,2,3,3,3,4,5,6,6}));
    }
   public static int solution(int[] array) {
		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
		int maxVal = -1, maxValCnt = 0;
		for (int i = 0; i < array.length; i++) {
			int t = map.getOrDefault(array[i], 0) + 1;//form: (key, value) => 찾는 key가 존재하면 해당 key에 매핑되어 있는 값을 반환하고, 그렇지 않으면 디폴트 값이 반환
			map.put(array[i], t);//key-value있으면 value 덮어씌워짐
			if(maxValCnt<t) {maxVal = array[i]; maxValCnt = t;}
		}
		for(Integer i: map.keySet()) {//개수 같은 원소가 2개 이상 있는지 확인
			if(map.get(i)==maxValCnt && i!=maxVal) return -1;//실제 찾은 max원소랑 다른데 개수는 같다면 -1 반환
		}
		return maxVal;//그렇지 않으면 최빈값 찾음
	}
}