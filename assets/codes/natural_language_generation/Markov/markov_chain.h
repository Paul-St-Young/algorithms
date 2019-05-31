#include <cstdlib>
#include <ctime>
#include "markov_state.C"

class MarkovChain {
    public:
        MarkovChain(MarkovState & state);
        MarkovState & add_state(string name);

        MarkovState * curr_state;
//        void set_state(MarkovState & state) {curr_state=&state;}
        void set_rand_state();
        void evolve() {curr_state=curr_state->choose_next_state();}
        void print();

    private:
        MarkovState* * states;
        int num_states;
};
