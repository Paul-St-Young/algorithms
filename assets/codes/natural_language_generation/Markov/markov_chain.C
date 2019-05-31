#include <cmath>
#include "markov_chain.h"

MarkovChain::MarkovChain(MarkovState & state)
    : num_states(1), curr_state(&state) {
    states=new MarkovState * [1];
    states[0]=&state;
    srand(time(NULL));
}

MarkovState & MarkovChain::add_state(string name) {

    // if it's already in the chain, return existing state
    for (int i=0; i<num_states; i++) {
        if (states[i]->name==name)
            return *(states[i]);
    }

    // otherwise, create, add, and return the new state
    num_states++;
    MarkovState* * new_states=new MarkovState * [num_states];

    // copy old states to new array
    for (int i=0; i<num_states-1; i++)
        new_states[i]=states[i];

    // add new state
    new_states[num_states-1]=new MarkovState(name);

    // update member variable
    delete states;
    states=new_states;

    // return newly added state
    return *(new_states[num_states-1]);
}

void MarkovChain::set_rand_state() {
    // set random initial state
    double random_num=rand();
    int random_int = (int) floor(random_num/RAND_MAX*num_states);
    curr_state=states[random_int];
}

void MarkovChain::print() {
    cout << "the chain contains the following states:" << endl;
    for (int i=0; i<num_states; i++) {
        cout << "\t";
        states[i]->print();
    }
}
