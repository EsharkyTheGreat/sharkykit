#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    char buf[0x20];
    fgets(buf, 0x1024, stdin);
    return 0;
}
