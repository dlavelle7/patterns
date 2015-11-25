// Strategy Design Pattern

public class Client {
	
	private double salary;
	private TaxStrategy taxStrategy;

	public Client(double salary) {
		this.salary = salary;
		setTaxStrategy(salary);
	}

	private void setTaxStrategy(double salary) {
		if (salary < 32000){
			this.taxStrategy = new LowerTaxStrategy();
		}
		else {
			this.taxStrategy = new HigherTaxStrategy();
		}
		
	}
	
	public double payTax(){
		return this.taxStrategy.calculateTax(salary);
	}

}
