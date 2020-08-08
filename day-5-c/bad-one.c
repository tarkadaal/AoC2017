#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ae_load_file_to_memory(const char *filename, char **result)
{
    int size = 0;
    FILE *f = fopen(filename, "rb");
    if (f == NULL)
    {
        *result = NULL;
        return -1; 
    }
    fseek(f, 0, SEEK_END);
    size = ftell(f);
    fseek(f, 0, SEEK_SET);
    *result = (char *)malloc(sizeof(char) * (size + 1));
    if (size != fread(*result, sizeof(char), size, f))
    {
        free(*result);
        return -2; 
    }
    fclose(f);
    (*result)[size] = 0;
    return size;
}

int main(void)
{
    int fill_index = 0;
    const char *delim = "\n";
    char *token = NULL;
    char *content = NULL;

    ae_load_file_to_memory("input.txt", &content);

    token = strtok(content, delim);

    while (token != NULL)
    {
        fill_index++;
        token = strtok(NULL, delim);
    }
    printf("Fill index %d\n", fill_index);
}