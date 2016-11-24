/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
	
		
		Vector<Integer> denom = new Vector<Integer>();
		denom.addElement(new Integer(2));
		denom.addElement(new Integer(1));
		denom.addElement(new Integer(5));
		denom.addElement(new Integer(10));
		
		int sum = 67;
		
		int numOfCoins = Ideone.findMinCoins(denom, sum);
		System.out.println("Number of Coins is : " +numOfCoins);
	}
	
	public static int findMinCoins(Vector<Integer> denom, int sum) {
		
		int count = 0;
		Collections.sort(denom, new Comparator<Integer>(){
			public int compare(Integer i1, Integer i2){
				if(i1 > i2)
					return -1;
				else
					return 1;
			}
		});

		for(Integer i : denom) {
			while (true) {
				count += sum / ((int)i);
				sum = sum % ((int) i);
			
				if(sum <= 0 || sum < i)
					break;
			}
		}
		
		return count;
	}
	
}
