__kernel void complement(__global char *A, __global int *B)
{
    // Get the index of the current work item
    int tid = get_global_id(0);

    // Do the operation
    char *num_str = &A[tid * 32]; // Assuming a maximum length of 32 for binary strings
    int complement = 0;
    int pow = 1;

    // Find the length of the binary string
    int numDigits = 0;
    while (num_str[numDigits] != '\0')
    {
        numDigits++;
    }

    // Iterate through each digit in reverse order
    for (int i = numDigits - 1; i >= 0; i--)
    {
        int bit = num_str[i] - '0';
        bit = (bit == 0) ? 1 : 0; // Flip the bit for 1's complement
        complement += bit * pow;
        pow *= 10;
    }

    B[tid] = complement;
}
