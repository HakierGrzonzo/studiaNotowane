#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
void zapiszFun(double (*f)(double x), double a, double b, int n, string nazwaPliku)
{
    ofstream file;
    file.open(nazwaPliku);
    if (!file.is_open() || b <= a || n < 1) throw std::runtime_error("heh, nope");
    for (double i = a; i < b; i += ((b - a) / ((double)n)))
    {
        file << i << '\t' << f(i) << ';' << endl;
    }
    file.close();
}

vector<vector<double>> readArrsFromFile(string filename)
{
    auto res = vector<vector<double>>();
    res.push_back(vector<double>());
    res.push_back(vector<double>());
    ifstream file;
    file.open(filename);
    if (!file.is_open()) throw std::runtime_error("Plik could not be read");
    while (!file.eof())
    {
        string line;
        getline(file, line);
        try
        {
            string a = line.substr(0, line.find('\t'));
            string b = line.substr(line.find('\t') + 1, line.size() - line.find('\t') - 2);
            double arg = stod(a);
            double val = stod(b);
            res[0].push_back(arg);
            res[1].push_back(val);
        }
        catch (exception& e)
        {
            break;
        }
    }
    file.close();
    return res;
}

double somefunc(double arg)
{
    return arg * arg + 3;
}

int main(int argc, char** argv)
{
    zapiszFun(somefunc, 0, 1, 25, "plswrk.txt");
    auto result = readArrsFromFile("plswrk.txt");
    for (int i = 0; i < result[0].size(); i++)
    {
        cout << "f("<< result[0][i] << ") =\t"<< result[1][i] << endl;
    }
    cout << "-------" << endl;
    for (int i = 0; i < result[0].size() - 1; i++)
    {
        cout << "f'("<< result[0][i] << ") =\t"<< (result[1][i+1] - result[1][i]) / (result[0][i+1] - result[0][i]) << endl;
    }
}
