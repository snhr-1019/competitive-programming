package QualificationRound2010;

import static java.lang.Integer.parseInt;

import java.io.BufferedReader;
import java.io.FileReader;

public class SnapperChain {
	public static void main(String[] args) {
		try {
			String filename = "QualificationRound2010\\A-small-attempt1.in";
			BufferedReader br = new BufferedReader(new FileReader(filename));

			// ñ‚ëËêî
			int T = parseInt(br.readLine());

			for (int n = 0; n < T; n++) {
				String[] strArr = br.readLine().split(" ");
				int N = Integer.parseInt(strArr[0]);
				long K = Integer.parseInt(strArr[1]);
				boolean result = solve(N, K);
				System.out.print("Case #" + (n+1) + ": ");
				if (result) {
					System.out.println("ON");
				} else {
					System.out.println("OFF");
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	static boolean solve(int N, long K) {
		// 0ÇÕìdåπ
		boolean[] snappers = new boolean[N+1];

		snappers[0] = true;

		for (long k = 0; k < K; k++) {
			//show(snappers);

			boolean[] newState = (boolean[])snappers.clone();

			for (int n = 1; n < N+1; n++) {
				if ( !snappers[n-1]) {
					break;
				}
				newState[n] = !snappers[n];
			}

			snappers = newState;
		}
		//show(snappers);

		// ëSïîÇÃsnapperÇ™trueÇÃÇ∆Ç´ÇæÇØtrue
		for (boolean snapper : snappers) {
			if (!snapper) { return false; }
		}
		return true;
	}

	static void show(boolean[] snappers) {
		for (boolean snapper : snappers) {
			System.out.print(snapper + " ");
		}
		System.out.println();
	}

}

//class Snapper {
//	boolean state = false;
//
//	void toggle() {
//		if (power) {
//			state = !state;
//		}
//	}
//
//	boolean isReceivingPower() {
//		return (power && state);
//	}
//}
