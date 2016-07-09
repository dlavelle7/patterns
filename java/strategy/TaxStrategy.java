// Strategy pattern example for income tax

class Client {
	
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

interface TaxStrategy {
	
	public double calculateTax(double salary);

}

class HigherTaxStrategy implements TaxStrategy {

	@Override
	public double calculateTax(double salary) {
		double higher = (salary - 3200) * 0.40;
		return (3200 * 0.20) + higher;
	}

}

class LowerTaxStrategy implements TaxStrategy{

	@Override
	public double calculateTax(double salary) {
		return salary * 0.20;
	}

}