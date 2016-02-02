/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
	
		
	String s1 = "Hello there man";
	String s2 = "there";
	
	int index = Ideone.isSubstring(s2, s1);
		
	System.out.println("Is s2 : \"" +s2 + "\" substring of s1 : \"" +s1 + "\"? : " +index);
	}
	
	public static int isSubstring(String s1, String s2) {
		
		int index;
		
		if (s1 == null || s2 == null || s2.length() < s1.length()) {
			return -1;
		}
		
		for(int i = 0; i < s2.length(); i++) {
			if ((s2.charAt(i)) == (s1.charAt(0))) {
				index = i;
				int j = 1;
				for( j = 1 ; j < s1.length() ; j++) {
					i++;
					if ((s2.charAt(i)) == (s1.charAt(j))) {
						continue;
					}
					break;
				}
				if (j == s1.length()) {
					return index;
				}
				else 
					continue;
			}
		}
		
		return -1;
	}
	
}
