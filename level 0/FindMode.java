import java.util.*;

class FindMode {
    public static void main(String[] args) {
        System.out.println(solution(new int[] {2,2,3,3,3,4,5,6,6}));
    }
   public static int solution(int[] array) {
		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
		int maxVal = -1, maxValCnt = 0;
		for (int i = 0; i < array.length; i++) {
			int t = map.getOrDefault(array[i], 0) + 1;
			map.put(array[i], t);
			if(maxValCnt<t) {maxVal = array[i]; maxValCnt = t;}
		}
		for(Integer i: map.keySet()) {
			if(map.get(i)==maxValCnt && i!=maxVal) return -1;
		}
		return maxVal;
	}
}