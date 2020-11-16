#include <iostream>
#include <iomanip>
#include <random>

#define board_size 20

std::random_device device;
std::mt19937 generator(device());
std::uniform_int_distribution<int> distributionXY(0, board_size);

int randomXY()
{
    return distributionXY(generator);
}

bool randomDirection()
{
    return (distributionXY(generator) > (board_size / 2));
}

bool ustaw_masztowiec (int plansza[board_size][board_size], int x, int y, int n, bool vertical)
{
    if ((!vertical && board_size - x >= n && y < board_size) || (vertical && board_size - y >= n && x < board_size))
    {
        for (int i = 0; i < n; i++)
        {
            if (vertical && plansza[x][y + i] != 0) return false;
            if (!vertical && plansza[x + i][y] != 0) return false;
        }
        for (int x_pos = 0; x_pos < board_size; x_pos++)
        {
            for (int y_pos = 0; y_pos < board_size; y_pos++)
            {
                if (vertical && x_pos == x && y_pos - y < n && y_pos >= y)
                {
                    plansza[x_pos][y_pos] = n;
                }
                else if (!vertical && y_pos == y && x_pos - x < n && x_pos >= x)
                {
                    plansza[x_pos][y_pos] = n;
                }
                else if (!vertical && (y_pos == y + 1 || y_pos == y - 1) && x_pos >= x - 1 && x_pos <= x + n)
                {
                    plansza[x_pos][y_pos] = -1;
                }
                else if (vertical && (x_pos == x + 1 || x_pos == x - 1) && y_pos >= y - 1 && y_pos <= y + n)
                {
                    plansza[x_pos][y_pos] = -1;
                }
                else if (vertical && x_pos == x && (y_pos == y -1 || y_pos == y + n ))
                {
                    plansza[x_pos][y_pos] = -1;
                }
                else if (!vertical && y_pos == y && (x_pos == x -1 || x_pos == x + n ))
                {
                    plansza[x_pos][y_pos] = -1;
                }
            }
        }
        return true;
    }
    else return false;
}

void ustawStatki(int plansza[board_size][board_size])
{
    while(!ustaw_masztowiec(plansza, randomXY(), randomXY(), 4, randomDirection()))
    {}
    for (int i = 0; i < 20; i++)
    {
        while(!ustaw_masztowiec(plansza, randomXY(), randomXY(), 3, randomDirection()))
        {}
    }
    for (int i = 0; i < 3; i++)
    {
        while(!ustaw_masztowiec(plansza, randomXY(), randomXY(), 2, randomDirection()))
        {}
    }
    for (int i = 0; i < 4; i++)
    {
        while(!ustaw_masztowiec(plansza, randomXY(), randomXY(), 1, randomDirection()))
        {}
    }
}

int main()
{
    int plansza[board_size][board_size] {};
    ustawStatki(plansza);
    for (int i = 0; i < board_size; i++)
    {
        for(int j = 0; j < board_size; j++)
        {
            std::cout << std::setw(3) << plansza[i][j];
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;

    for (int i = 0; i < board_size; i++)
    {
        for(int j = 0; j < board_size; j++)
        {
            std::cout << (plansza[i][j] > 0 ? 'X' : '-');
        }
        std::cout << std::endl;
    }
}