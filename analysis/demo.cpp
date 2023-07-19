// NOTE: TRY fast-cpp-csv-parser

#include <fstream>
#include <sstream>
#include <queue>
#include <vector>

using namespace std;

vector<string> split(const string &s, char delimiter) {
    vector<string> tokens;
    string token;
    istringstream tokenStream(s);
    while (getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

int main() {
    ifstream file("data.csv");
    vector<queue<string>> columns;
    string line;

    if (getline(file, line)) {
        vector<string> firstRow = split(line, ',');
        columns.resize(firstRow.size());

        for (size_t i = 0; i < firstRow.size(); ++i) {
            columns[i].push(firstRow[i]);
        }
    }

    while (getline(file, line)) {
        vector<string> row = split(line, ',');

        for (size_t i = 0; i < row.size(); ++i) {
            columns[i].push(row[i]);
        }
    }

    file.close();

    return 0;
}
