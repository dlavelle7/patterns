package hello_world;

import org.junit.Test;
import static org.junit.Assert.*;

public class TaxStrategyTest {

	@Test
	public void testPayTax() {
		Client lowClient = new Client(20000);
		assertTrue(lowClient.payTax() == 4000);
		
		Client hiClient = new Client(40000);
		System.out.println(hiClient.payTax());
		assertTrue(hiClient.payTax() == 15360);
	}

}
