#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);
char* decimalTotinary(int decimal);
int main(void)
{
    // TODO
    string message; // Assuming a maximum message length of 100 characters
    message=get_string("Message: ");

    for (int line = 0; line < strlen(message); line++)
    {
        int aski = (int)message[line];
        char* bit = decimalTotinary(aski);

        for (int i = 0; i < 8; i++)
        {
            print_bulb((int)bit[i] -48);
        }
printf("\n");
        // Free the allocated memory
        free(bit);
    }

    return 0;
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
char* decimalTotinary(int decimal)
{
    char* binaryString = (char*)malloc(9); // 8 bits + '\0' null terminator

    for (int i = 7; i >= 0; i--)
    {
        binaryString[i] = (decimal % 2) + '0';
        decimal = decimal / 2;
    }

    binaryString[8] = '\0'; // Null terminator for the string

    return binaryString;
}
