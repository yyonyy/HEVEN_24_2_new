#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <algorithm>

using namespace std;

class Dicegame
{
public:
    Dicegame() {
        for (int i = 0; i < 6; ++i) {
            dice_num[i] = 0;
        }
    }

    void roll_dice() {
        cin >> N;
        srand((unsigned int)time(NULL));
        for (int i=0; i<N; i++) {
            dice = rand()%6;
            dice_num[dice]++;
        }
    };

    void print_result() {
        for (int i = 0; i < 6; ++i) {
            cout << "Dice number " << i+1 << " : " << dice_num[i] << endl;
        }

        int first_largest = 0;
        int second_largest = 0;
        
        first_largest = *max_element(dice_num.begin(), dice_num.end());

        for (int num : dice_num) {
            if (num < first_largest && num > second_largest) {
                second_largest = num;
            }
        }

        for (int i = 0; i < 6; ++i) {
            if (dice_num[i] == second_largest) {
                cout << "Second Largest Number : " << (i+1) << endl;
            }
        }
    };

private:
    int N;
    vector<int> dice_num = {0, 0, 0, 0, 0, 0};
    int dice;
};


int main() {
    Dicegame dicegame;
    dicegame.roll_dice();
    dicegame.print_result();
};