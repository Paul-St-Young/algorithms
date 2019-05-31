#include <iostream>
using namespace std;

class MarkovState {

    public:
        string name;
        MarkovState(string thename="") : name(thename) {};

        void add_next_state(MarkovState * next_state);
        MarkovState * choose_next_state();
        void print() const;

    private:
        MarkovState* * next_states=NULL;
        int num_next_states=0;

        double * probs=NULL;
        int * prob_numerators=NULL;
        float prob_denominator=0;

        int find_next_state(string thename) const;
};
