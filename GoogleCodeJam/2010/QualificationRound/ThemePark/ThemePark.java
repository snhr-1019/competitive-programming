
import static java.lang.Integer.parseInt;

import java.io.BufferedReader;
import java.io.FileReader;

public class ThemePark {
	public static void main(String[] args) {
		try {
			String filename = "C-small-attempt1.in";
			BufferedReader br = new BufferedReader(new FileReader(filename));

			// ñ‚ëËêî
			int T = parseInt(br.readLine());

			for (int t = 0; t < T; t++) {
				String[] strArr = br.readLine().split(" ");
				int roundNum = parseInt(strArr[0]); // R
				int capacity = parseInt(strArr[1]); // k
				int groupNum = parseInt(strArr[2]); // N

				strArr = br.readLine().split(" ");
				int[] group = new int[strArr.length];
				for (int i = 0; i < groupNum; i++) {
					group[i] = parseInt(strArr[i]);
				}

				// Ç±Ç±Ç©ÇÁÉAÉãÉSÉäÉYÉÄ

				int top = 0;
				long money = 0;
				for (long r = 0; r < roundNum; r++) {
					// èÊé‘êlêî
					int personNum = 0;
					for (int i = 0; i < groupNum; i++) {
						if (personNum + group[top] > capacity) { break; }
						personNum += group[top];
						top = (top+1) % groupNum;
					}
					money += personNum;
				}

				System.out.println("Case #" + (t+1) + ": " + money);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
