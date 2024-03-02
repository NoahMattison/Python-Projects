public class Clock {
	
	//Attribute
	private int hour;
	private int minute;
	private int second;
	private String shape;
	private String backgroundColor;
	private String numColor;
	
	//Constructor
	Clock(int hour, int minute, int second, String shape, String backgroundColor, String numColor) {
		this.hour = hour;
		this.minute = minute;
		this.second = second;
		this.shape = shape;
		this.backgroundColor = backgroundColor;
		this.numColor = numColor;
	}
	
	//Getters or Accessors
	//Getters or Accessors
	public int getHour() { return this.hour; }
	public int getMinute() { return this.minute; }
	public int getSecond() { return this.second; }
	public String getShape() { return this.shape; }
	public String getBackgroundColor() { return this.backgroundColor; }
	public String getNumColor() { return this.numColor; }


	//Setters or Mutators
	public void setHour(int hour) { this.hour = hour; }
	public void setMinute(int minute) { this.minute = minute; }
	public void setSecond(int second) { this.second = second; }
	public void setShape(String shape) {this.shape = shape; }
	public void setBackgroundColor(String backgroundColor) { this.backgroundColor = backgroundColor; }
	public void setNumColor(String numColor) {this.numColor = numColor; }
	
	
	//Other Methods
	public void displayTime() {
		System.out.printf("%02d:%02d:%02d", hour, minute, second);
	}

}
