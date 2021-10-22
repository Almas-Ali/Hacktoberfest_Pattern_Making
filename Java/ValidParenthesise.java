package com.company;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Map;
import java.util.Objects;

public class ValidParenthesise {

    public static void main(String[] args) {
        System.out.println(isValid("([)]"));
    }

    static final Map<Character, Character> charMap = Map.of('(', ')', '{', '}', '[', ']');

    public static boolean isValid(String s) {
        Deque<Character> chars = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            Character last = chars.isEmpty() ? '#' : chars.peek();

            if (Objects.equals(s.charAt(i), charMap.get(last))) {
                chars.pop();
            } else {
                chars.push(s.charAt(i));
            }
        }
        return chars.isEmpty();
    }

}
