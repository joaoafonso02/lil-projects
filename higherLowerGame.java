import java.util.Scanner;

public class p44 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("\ntry to guess the number I have!");
				
		int x, x1, secret;
		int cont = 0;
		
		secret = (int)(100.0 * Math.random()) + 1;
		
		System.out.println(secret);	
		do {	
			System.out.print("\nnumber: ");
			
			x = sc.nextInt();
			
		
			
				if (x <= 100 && x >= 1) {
				
					
					 if (secret > x ){
						System.out.println("The number u introduce is too bellow comparative to the number I have");
					
					} else if (secret < x) {
						System.out.println("The number u introduce is too above comparative to the number I have");
					}
					
					
					
				} else { 
					System.out.println("The number u wrote it is not between 1 and 100. \nTry agin: ");
				
				}	
			cont++;
				
		} while ((x != secret));
			
		 System.out.print("\nCongratss!!You guessed the number" + "\nNumber of tries: " + cont);
				
}
}
