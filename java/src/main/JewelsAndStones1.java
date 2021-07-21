package main;

import java.util.HashSet;
import java.util.Set;

class JewelsAndStones1 {
    public int numJewelsInStones(String J, String S) {
        int count =0;
        Set<Character> set = new HashSet();
        for(char ch : J.toCharArray() )
            set.add(ch);
        for(char ch : S.toCharArray() ){
            if( set.contains(ch) )
                count++;
        }
        return count;
    }
}