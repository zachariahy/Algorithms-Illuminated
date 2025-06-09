#include <stdio.h>
#include <stdlib.h>

// Function to print an array
void printArray(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Merge function to combine two sorted arrays
int* Merge(int *nums1, int nums1Size, int *nums2, int nums2Size) {
    int n = nums1Size + nums2Size, i = 0, j = 0;
    int* returnArray = malloc(sizeof(int) * n);

    if (!returnArray) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    for (int k = 0; k < n; k++) {
        if (i == nums1Size) {
            returnArray[k] = nums2[j++];
        } else if (j == nums2Size) {
            returnArray[k] = nums1[i++];
        } else if (nums1[i] < nums2[j]) {
            returnArray[k] = nums1[i++];
        } else {
            returnArray[k] = nums2[j++];
        }
    }
    return returnArray;
}

// MergeSort function
int* MergeSort(int* nums, int numsSize) {
    if (numsSize < 2) {
        int* singleElement = malloc(sizeof(int));
        if (!singleElement) {
            fprintf(stderr, "Memory allocation failed\n");
            exit(EXIT_FAILURE);
        }
        *singleElement = nums[0];
        return singleElement;
    }

    int nums1Size = numsSize / 2;
    int nums2Size = numsSize - nums1Size;
    
    // Allocate and copy data for left and right halves
    int* firstHalf = malloc(sizeof(int) * nums1Size);
    int* secondHalf = malloc(sizeof(int) * nums2Size);

    if (!firstHalf || !secondHalf) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < nums1Size; i++) {
        firstHalf[i] = nums[i];
    }
    for (int i = 0; i < nums2Size; i++) {
        secondHalf[i] = nums[i + nums1Size];
    }

    // Recursively sort both halves
    int* sortedFirst = MergeSort(firstHalf, nums1Size);
    int* sortedSecond = MergeSort(secondHalf, nums2Size);

    // Merge the sorted halves
    int* sortedArray = Merge(sortedFirst, nums1Size, sortedSecond, nums2Size);

    // Free allocated memory
    free(firstHalf);
    free(secondHalf);
    free(sortedFirst);
    free(sortedSecond);

    return sortedArray;
}

// Test function for MergeSort
void testMergeSort() {
    int nums1[] = {5, 2, 9, 1, 10, 3, 9, 0};
    int size1 = sizeof(nums1) / sizeof(nums1[0]);

    printf("Original array: ");
    printArray(nums1, size1);

    int* sortedArray = MergeSort(nums1, size1);

    printf("Sorted array: ");
    printArray(sortedArray, size1);

    free(sortedArray);
}

// Main function
int main() {
    testMergeSort();
    return 0;
}

