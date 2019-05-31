#include <fstream>
#include "markov_chain.C"

int main(int argc, char **argv) {

    // check command line arguments
    if (argc<4) {
        cout << "Please specify the path to a text file, length of output, and value of n." << endl;
        cout << "Example: " << argv[0] << " sample_text 100 3" << endl;
        return 0;
    }

    // open text file
    ifstream file;
    file.open(argv[1]);
    int num_words = strtol(argv[2],NULL,10);

    // initialize markov chain
    int n=strtol(argv[3],NULL,10);
    string prev_word [n-2], state_name, word;
    file >> state_name;
    for (int i=0; i<n-2; i++) {
        file >> prev_word[i];
        state_name += " "+prev_word[i];
    }

    MarkovState * first_state = new MarkovState(state_name);
    MarkovChain chain(*first_state);

    // build markov chain
    MarkovState * prev_state = first_state;
    MarkovState * state;
    while (file >> word) {
        state_name = prev_word[0];
        for (int i=0; i<n-3; i++) {
            prev_word[i] = prev_word[i+1];
            state_name += " "+prev_word[i];
        }
        prev_word[n-3]=word;
        state_name += " "+word;

        state=&chain.add_state(state_name);
        prev_state->add_next_state(state);
        prev_state=state;
    }

    // connect last state to first state
    state->add_next_state(first_state);

    // for debugging -- print each state, its possible next states, and their probabilities
//    chain.print();

    // randomly choose first word and capitalize it
    chain.set_rand_state();
    string first_word=chain.curr_state->name;
    first_word[0]=toupper(first_word[0]);
    cout << first_word.substr(0, first_word.find(" ")) << " ";

    // run markov chain!
    for (int i=0; i<num_words-2; i++) {
        chain.evolve();
        string curr_words = chain.curr_state->name;
        cout << curr_words.substr(0, curr_words.find(" ")) << " ";
    }

    // last word -- check punctuation
    chain.evolve();
    string last_word=chain.curr_state->name;
    char last_letter=last_word.back();
    if (last_letter == '.' or last_letter == ',' or last_letter == ';' or last_letter == ':' or last_letter == '?' or last_letter == '!')
        last_word.pop_back();
    cout << last_word << "." << endl;

    return 0;
}
