#include "markov_state.h"

int MarkovState::find_next_state(string thename) const {
    
    // return index of state with requested name
    for (int i=0;i<num_next_states;i++) {
        if (next_states[i]->name==thename)
            return i;
    }

    // state not found; return -1
    return -1;
}

void MarkovState::add_next_state(MarkovState * next_state) {
   
    prob_denominator++; 
    int next_state_ind=find_next_state(next_state->name);

    // if this is a new state, add it to the arrays and update probabilities
    if (next_state_ind==-1) {
        num_next_states++;
 
       // allocate new arrays
        MarkovState* * new_next_states = new MarkovState * [num_next_states];
        int * new_prob_numerators = new int[num_next_states];
        double * new_probs = new double[num_next_states];

        // copy existing next states
        for (int i=0;i<num_next_states-1;i++) {
            new_next_states[i]=next_states[i];
            new_prob_numerators[i]=prob_numerators[i];         // keep old numerators the same
            new_probs[i]=prob_numerators[i]/prob_denominator; // new probability uses incremented denominator
        }

        // add new state
        new_next_states[num_next_states-1]=next_state;
        new_prob_numerators[num_next_states-1]=1;
        new_probs[num_next_states-1]=1/prob_denominator;

        // free old memory and update member variables
        delete next_states;
        delete prob_numerators;
        delete probs;
        next_states=new_next_states;
        prob_numerators=new_prob_numerators;
        probs=new_probs;

    }

    // if this is an existing state, just update probabilities
    else {
        prob_numerators[next_state_ind]++;
        for (int i=0;i<num_next_states;i++)
            probs[i]=prob_numerators[i]/prob_denominator;   // new probability uses incremented denominator
    }
}

MarkovState * MarkovState::choose_next_state() {

    // should always have at least one next state to choose from
    if (num_next_states==0) {
        cout << "warning: no next states added for state " << name << endl;
        return this;
    }

    // generate random number from 0 to 1
    double random_num=rand();
    random_num=random_num/RAND_MAX;

    // select next state based on random number
    int next_ind=0;
    double cumm_prob=probs[0];
    while (cumm_prob < random_num) {
        next_ind++;
        cumm_prob+=probs[next_ind];
    }

    return next_states[next_ind];
}

void MarkovState::print() const {
    //print each possible next state with its probability
    cout << "state " << name << "(" << this << ") " << " will go to..." << endl;
    for (int i=0; i<num_next_states; i++)
        cout << "\t\tstate " << next_states[i]->name << "(" << (next_states[i]) << ") " << " with probability " << probs[i] << endl;
}
