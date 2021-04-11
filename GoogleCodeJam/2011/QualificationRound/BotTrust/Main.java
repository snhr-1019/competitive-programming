import java.io.File;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Collections;
import java.util.Date;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	private final static String SAMPLE = "sample.txt";
	private final static String SMALL = "A-small-practice.in";
	private final static String LARGE = "A-large-practice.in";

	public static int N;
	public static Operation[] opeArr;

	public static void main(String[] args) {
		try {
			File in = new File("A-small-attempt0.in");
			Scanner sc;
			sc = new Scanner(in);
			// sc.useDelimiter("\\r\\n|\\n");
			int T = sc.nextInt();

			for (int caseNum = 0; caseNum < T; caseNum++) {
				solve(sc, caseNum);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	private static void solve(Scanner sc, int caseNum) throws ParseException {
		N = sc.nextInt();

		opeArr = new Operation[101];
		opeArr[0] = new Operation("", -1);
		for (int i = 1; i < N + 1; i++) {
			opeArr[i] = new Operation(sc.next(), sc.nextInt());
		}

		Robot orange = new Robot("O", 1, 0);
		Robot blue = new Robot("B", 1, 0);
		orange.findNextOperation();
		blue.findNextOperation();
		int ans = 0;

		while (true) {
			boolean isPushedO = orange.execute(blue);
			boolean isPushedB = blue.execute(orange);
			ans++;

			if (isPushedO) {
				orange.findNextOperation();
			}

			if (isPushedB) {
				blue.findNextOperation();
			}

			if (orange.ope == 101 && blue.ope == 101) {
				break;
			}
		}

		System.out.println("Case #" + (caseNum + 1) + ": " + ans);
	}

	private static class Robot {
		String color;
		int pos;
		int ope;

		public Robot(String color, int pos, int ope) {
			this.color = color;
			this.pos = pos;
			this.ope = ope;
		}

		public void findNextOperation() {
			for (int i = ope + 1; i < N + 1; i++)
				if (this.color.equals(opeArr[i].color)) {
					ope = i;
					return;
				}
			ope = 101;
		}

		public boolean execute(Robot anotherRobot) {
			if (ope == 101) {
				return false;
			}

			if (pos == opeArr[ope].pos) {
				if (this.ope < anotherRobot.ope) {
					return true;
				}
			} else if (pos < opeArr[ope].pos) {
				pos++;
			} else {
				pos--;
			}

			return false;
		}
	}

	private static class Operation {
		String color;
		int pos;

		public Operation(String color, int pos) {
			this.color = color;
			this.pos = pos;
		}

		@Override
		public String toString() {
			return "[" + color + " , " + pos + "]";
		}
	}

}
