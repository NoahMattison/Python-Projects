public class WashingMachine {

	private String brand;
	private String model;
	private double price;
	
	//constructor
	WashingMachine(String brand, String model, double price){
		this.brand = brand;
		this.model = model;
		this.price = price;
	}
	
	//Accessors
	public String getBrand() {return this.brand;}
	public String getModel() {return this.model;}
	public double getPrice() {return this.price;}
	
	//Mutators
	public void setBrand(String brand) {this.brand = brand;}
	public void setModel(String model) {this.model = model;}
	public void setPrice(double price) {this.price = price;}

	//Sale Price Method
	public double salePrice() { return this.price * 0.95;}

}
