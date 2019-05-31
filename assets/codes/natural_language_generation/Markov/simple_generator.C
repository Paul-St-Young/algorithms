#include <fstream>
#include "markov_chain.C"

int main(int argc, char **argv) {

    // check command line arguments
    if (argc<3) {
        cout << "Please specify the path to a text file and length of output." << endl;
        cout << "Example: " << argv[0] << " sample_text 100" << endl;
        return 0;
    }

    // open text file
    ifstream file;
    file.open(argv[1]);
    int num_words = strtol(argv[2],NULL,10);

    // initialize markov chain
    string word, prev_word;
    file >> prev_word;
    MarkovState * first_state = new MarkovState(prev_word);
    MarkovChain chain(*first_state);

    // build markov chain
    MarkovState * prev_state = first_state;
    MarkovState * state;
    while (file >> word) {
        state=&chain.add_state(word);
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
    cout << first_word << " ";

    // run markov chain!
    for (int i=0; i<num_words-2; i++) {
        chain.evolve();
        cout << chain.curr_state->name << " ";
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
