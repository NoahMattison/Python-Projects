public class WMTestMattison {
    public static void main(String[] args) {
        // creates 3 instances of WashingMachine
        WashingMachine[] wm = new WashingMachine[3];
        // Stores instances in array
        wm[0] = new WashingMachine("Whirlpool", "baby", 7843);
        wm[1] = new WashingMachine("LG", "i hate java", 234768780);
        wm[2] = new WashingMachine("poop", "poopie", 1);

        System.out.printf("%-15s%-15s%-15s%-15s\n", "Brand", "Model", "Price", "Sale Price");

        for(WashingMachine machine : wm) {
            System.out.printf("%-15s%-15s%-15.2f%-15.2f\n", machine.getModel(), machine.getBrand(), machine.getPrice(), machine.salePrice());
        }
    }
}
