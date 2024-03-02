/**
 * @author Mrs. White
 * @desc   This program will use examples of methods, while and do while loops,
 * 		   sentinel values, conditional operator, toUpperCase for strings, and 
 * 		   character comparisons
 */

import java.util.Scanner;

public class Methods {
	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		//loop to determine play again feature
		while(true) {
			playGame();
			
			System.out.print("\nDo you want to play again?");
			String playAgain = input.nextLine().toUpperCase();
			if (playAgain.charAt(0) == 'N'){
				System.out.println("Goodbye!");
				break;
			}}
	}
	/**
	 *
	 * @param max1 = max value of random value
	 *
	 */
	public static int getRandom(int max1) {
		return (int)(Math.random()*max1) + 1;
	}

	/**
	 * Enables playing the game
	 *
	 *
	 */
	public static void playGame() {
		int answer = (int)(Math.random()*100) + 1;
		int guess;

		//loop to play game
		do {
			guess = getGuess();

			if (guess == answer) {
				System.out.println("You won!");
			}
			else {
				hiOrLo(guess,answer);
			}

		}while(guess != answer);
		}

	
	/**
	 * 
	 * @return	the user's input for guess
	 */
	//Example of a value returning method
	public static int getGuess() {
		Scanner input = new Scanner(System.in);
		System.out.print("Guess the number: ");
		int guess = input.nextInt();
		return guess;		
	}

	/**
	 * 
	 * @param guess		the value of the user's guess
	 * @param answer	the randomly generated integer
	 */
	//Example of a non-value returning method
	public static void hiOrLo(int guess, int answer) {
		//Example of conditional operator
		System.out.println(answer < guess ? "Lower" : "Higher");
		return;
	}
	
}
