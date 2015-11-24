
public class HigherTaxStrategy implements TaxStrategy {

	@Override
	public double calculateTax(double salary) {
		double higher = (salary - 3200) * 0.40;
		return (3200 * 0.20) + higher;
	}

}
