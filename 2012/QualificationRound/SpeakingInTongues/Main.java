import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
	public Scanner sc;
	public Map<Character, Character> mapping = new HashMap<Character, Character>();

	public static void main(String[] args) {
		Main m = new Main();
		m.start();
	}

	public void makeMapping() {
		String[] input = new String[3];
		input[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
		input[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
		input[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

		String[] output = new String[3];
		output[0] = "our language is impossible to understand";
		output[1] = "there are twenty six factorial possibilities";
		output[2] = "so it is okay if you want to just give up";

		for (int i = 0; i < output.length; i++) {
			char[] inArr = input[i].toCharArray();
			char[] outArr = output[i].toCharArray();
			for (int j = 0; j < inArr.length; j++) {
				if (inArr[j] != ' ' && !mapping.containsKey(inArr[j])) {
					mapping.put(inArr[j], outArr[j]);
				}
			}
			mapping.put('q', 'z');
			mapping.put('z', 'q');
		}
	}

	public void start() {
		makeMapping();
		sc = new Scanner(System.in);
		int t = sc.nextInt();
		sc.nextLine();
		for (int i = 1; i <= t; i++) {
			System.out.print("Case #" + i + ": ");
			solve();
		}
	}

	public String translate(String input) {
		char[] outArr = new char[input.length()];
		char[] inArr = input.toCharArray();
		for (int i = 0; i < inArr.length; i++) {
			if (inArr[i] == ' ') {
				outArr[i] = ' ';
			} else {
				outArr[i] = mapping.get(inArr[i]);
			}
		}

		return String.valueOf(outArr);
	}

	public void solve() {
		String s = sc.nextLine();
		System.out.println(translate(s));
	}
}
