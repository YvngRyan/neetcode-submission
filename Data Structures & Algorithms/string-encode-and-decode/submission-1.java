class Solution {

    public String encode(List<String> strs) {
        StringBuilder enc = new StringBuilder("");
        for (String s : strs) {
            int length = s.length();
            enc.append(length).append('#').append(s);
        }

        return enc.toString();
    }

    public List<String> decode(String str) {
        List<String> words = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            int j = i;
            while (str.charAt(j) != '#') {
                j++;
            }
            int length = Integer.parseInt(str.substring(i, j));
            i = j + 1;
            j = i + length;
            words.add(str.substring(i, j));
            i = j;
        }
        return words;
    }
}
