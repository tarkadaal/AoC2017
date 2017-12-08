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
        return -1; // -1 means file opening fail
    }
    fseek(f, 0, SEEK_END);
    size = ftell(f);
    fseek(f, 0, SEEK_SET);
    *result = (char *)malloc(size + 1);
    if (size != fread(*result, sizeof(char), size, f))
    {
        free(*result);
        return -2; // -2 means file reading fail
    }
    fclose(f);
    (*result)[size] = 0;
    return size;
}

int convert_strings_to_ints(char *content, int *instructions)
{
    int fill_index = 0;
    const char *delim = "\n";
    char *token;
    token = strtok(content, delim);

    while (token != NULL)
    {
        instructions[fill_index] = atoi(token);
        fill_index++;

        token = strtok(NULL, delim);
    }
    return fill_index;
}

int main(void)
{
    const int maze_size = 1044;
    int instructions[maze_size];
    int fill_index = 0;
    char *content;
    int size;
    size = ae_load_file_to_memory("input.txt", &content);
    printf("size %d\n", size);

    fill_index = convert_strings_to_ints(content, instructions);
    printf("Fille index %d\n", fill_index);

    int current_index = 0;
    int step_total = 0;
    int current_instruction = 0;
    while (-1 < current_index && current_index < fill_index )
    {
        step_total++;
        current_instruction = instructions[current_index];
        instructions[current_index] += current_instruction < 3 ? 1 : -1;
        current_index += current_instruction;
    };
    printf("%d\n", step_total);
}