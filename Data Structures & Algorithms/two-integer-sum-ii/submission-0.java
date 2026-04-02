class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int b = 0;
        int e = numbers.length - 1;

        while (b < e) {
            int sum = numbers[b] + numbers[e];
            if (sum < target) {
                b++;
            } else if (sum > target) {
                e--;
            } else {
                return new int[] {b + 1, e + 1};
            }
        }
        return new int[0];
    }
}
