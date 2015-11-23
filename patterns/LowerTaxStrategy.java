package hello_world;

public class LowerTaxStrategy implements TaxStrategy{

	@Override
	public double calculateTax(double salary) {
		return salary * 0.20;
	}

}
