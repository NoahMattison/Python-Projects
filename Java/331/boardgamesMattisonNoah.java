/**
 * Program Purpose: Board Games
 * Name: Noah Mattison
 * Date: 1/28/24
 * Section: CSC 331-002
 */

import java.util.Scanner;
import java.util.InputMismatchException;

public class boardgamesMattisonNoah {
    public static void main(String[] args) {
        displayMenu();
        int choice = getUserChoice();
        // Gets choice from user for what game
        System.out.println("That game takes  " + getPlayTime(choice) + " minutes to play.");
    }

    public static void displayMenu() {
        // handles the visual display of choices
        System.out.println("1. Monopoly\n2. Game of Life\n3. Pictionary\n4. Uno\n5. Root");
    }

    public static int getUserChoice() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Which one???: ");
        int input = 0;
        while (input < 1 || input > 5) {
            // Checks if the input is one of the accepted values, if not prompts the user again
            try {
                input = scanner.nextInt();
            }
            catch (InputMismatchException e) {
                scanner.nextLine();
                System.out.println("Try again!: ");
            }
        }
        return input;
    }
    public static double getPlayTime(int number) {
        switch (number) {
            case 1:
                return 120;
            case 2:
                return 60;
            case 3:
                return 90;
            case 4:
                return 10;
            case 5:
                return 60;
            default:
                return 0;
        }
    }
}
