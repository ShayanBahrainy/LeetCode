
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* convertTemperature(double celsius, int* returnSize) {
    *returnSize = 2;
    double* Johnny = malloc(sizeof(double) * (*returnSize));

    Johnny[0] = celsius + 273.15;
    Johnny[1] = (celsius * 1.80) + 32.0;

    return Johnny;
}