class Solution {
    public int countNumberofDigits(int n) {
        if (n >= 0) {
            return (int) Math.log10(n) + 1;
        } else {
            // To handle the case of negative number
            return (int) Math.log10(Math.abs(n)) + 1;
        }

    }
}
