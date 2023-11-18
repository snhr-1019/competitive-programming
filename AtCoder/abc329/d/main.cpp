#include <iostream>
#include <map>
#include <vector>

int main() {
    int N, M;
    std::cin >> N >> M;
    std::vector<int> A(M);
    for (int i = 0; i < M; ++i) {
        std::cin >> A[i];
    }

    std::map<int, int> votes;
    std::map<int, int> winner;
    for (int i = 0; i < M; ++i) {
        ++votes[A[i]];
        if (winner.empty() || votes[A[i]] > votes[winner.rbegin()->second] || 
            (votes[A[i]] == votes[winner.rbegin()->second] && A[i] < winner.rbegin()->second)) {
            winner[votes[A[i]]] = A[i];
        }
        std::cout << winner.rbegin()->second << std::endl;
    }

    return 0;
}
