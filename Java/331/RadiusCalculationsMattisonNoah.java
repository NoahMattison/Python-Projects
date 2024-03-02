/**
 * Program Purpose: Radius Calculations
 * Name: Noah Mattison
 * Date: 1/19/24
 * Section: CSC 331-002
 */

import java.util.Scanner;

public class RadiusCalculationsMattisonNoah {
    public static void main(String[] args) {
        System.out.println("Enter the minimum integer radius value: ");
        // Prompts user for min input
        Scanner sc = new Scanner(System.in);
        // Initializes the scanner
        int min = sc.nextInt();

        System.out.println("Enter the maximum integer radius value: ");
        // Prompts user for max input
        int max = sc.nextInt();

        System.out.println("Circle and Sphere Measurements for Integer Radius Values: ");
        System.out.printf("%15s %15s %15s %15s %15s\n", "Radius", "Circumference", "Area", "Surface Area", "Volume");

        // Loop that calculates values to be output
        for (int i = min; i <= max; i++) {
            double circumference = 2 * Math.PI * i;
            double area = Math.PI * Math.pow(i, 2);
            double surfaceArea = area * 4;
            double volume = ((double) 4/3) * Math.PI * Math.pow(i, 3);
            // outputs values
            System.out.printf("%15d %,15.2f %,15.2f %,15.2f %,15.2f\n", i, circumference, area, surfaceArea, volume);
        }

    }
}
