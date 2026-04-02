class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<Integer>[] freq = new List[nums.length + 1];
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        for (int n : map.keySet()) {
            freq[map.get(n)].add(n);
        }

        int[] result = new int[k];
        int count = 0;

        for (int i = freq.length - 1; i > 0 && count < k; i--) {
            for (int n : freq[i]) {
                result[count] = n;
                count++;
                if (count == k) {
                    return result;
                }
            }
        }
        return result;
    }
}
