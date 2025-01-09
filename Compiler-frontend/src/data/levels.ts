import { Difficulty } from '@/components/DifficultySelector';

interface Level {
  code: string;
  solution: string;
  hint: string;
}

type LevelsByDifficulty = {
  [key in Difficulty]: Level[];
};

export const LEVELS: LevelsByDifficulty = {
  easy: [
    {
      code: `#include <stdio.h>
int main() {
  printf("Hello World")
  return 0;
}`,
      solution: `#include <stdio.h>
int main() {
  printf("Hello World");
  return 0;
}`,
      hint: "Check the punctuation! C statements need a specific character at the end.",
    },
    {
      code: `#include <stdio.h>
int main() {
  int x = 5
  int y = 10;
  printf("%d", x + y);
  return 0;
}`,
      solution: `#include <stdio.h>
int main() {
  int x = 5;
  int y = 10;
  printf("%d", x + y);
  return 0;
}`,
      hint: "Look carefully at the first variable declaration. Is it properly terminated?",
    },
    {
      code: `#include <stdio.h>
int main() {
  int score = 100
  if(score >= 90)
    printf("You win")
  return 0;
}`,
      solution: `#include <stdio.h>
int main() {
  int score = 100;
  if(score >= 90)
    printf("You win");
  return 0;
}`,
      hint: "Multiple statements are missing the same punctuation mark. Can you spot them?",
    }
  ],
  medium: [
    {
      code: `#include <stdio.h>
int main() {
  for(int i = 0; i < 5; i++) {
    printf("%d", i)
  }
  return 0
}`,
      solution: `#include <stdio.h>
int main() {
  for(int i = 0; i < 5; i++) {
    printf("%d", i);
  }
  return 0;
}`,
      hint: "There are two syntax errors here. Check the printf and the return statement.",
    },
    {
      code: `#include <stdio.h>
int main() {
  int arr[5] = {1, 2, 3, 4, 5}
  for(int i = 0; i <= 5; i++) {
    printf("%d ", arr[i]);
  }
  return 0;
}`,
      solution: `#include <stdio.h>
int main() {
  int arr[5] = {1, 2, 3, 4, 5};
  for(int i = 0; i < 5; i++) {
    printf("%d ", arr[i]);
  }
  return 0;
}`,
      hint: "Check array declaration and loop condition. Remember arrays are 0-indexed!",
    },
    {
      code: `#include <stdio.h>
void printSquare(int n) {
  for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++)
      printf("*")
    printf("\\n");
  return;
}

int main() {
  printSquare(3);
  return 0;
}`,
      solution: `#include <stdio.h>
void printSquare(int n) {
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      printf("*");
    }
    printf("\\n");
  }
  return;
}

int main() {
  printSquare(3);
  return 0;
}`,
      hint: "Check the nested loops. Where should the braces be? Also look for missing semicolons.",
    }
  ],
  hard: [
    {
      code: `#include <stdio.h>
void swap(int a, int b) {
  int temp = a;
  a = b;
  b = temp;
}

int main() {
  int x = 5, y = 10;
  swap(x, y);
  printf("%d %d", x, y);
  return 0;
}`,
      solution: `#include <stdio.h>
void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

int main() {
  int x = 5, y = 10;
  swap(&x, &y);
  printf("%d %d", x, y);
  return 0;
}`,
      hint: "Think about pass by value vs pass by reference. How can we modify the original variables?",
    },
    {
      code: `#include <stdio.h>
struct Node {
  int data;
  struct Node* next;
};

int main() {
  struct Node* head = malloc(sizeof(struct Node));
  head->data = 1;
  head->next = NULL;
  printf("%d", head->data);
  return 0;
}`,
      solution: `#include <stdio.h>
#include <stdlib.h>
struct Node {
  int data;
  struct Node* next;
};

int main() {
  struct Node* head = malloc(sizeof(struct Node));
  head->data = 1;
  head->next = NULL;
  printf("%d", head->data);
  free(head);
  return 0;
}`,
      hint: "What header is missing for memory allocation? Also, remember to free allocated memory!",
    },
    {
      code: `#include <stdio.h>
#include <stdlib.h>

int* findMax(int arr[], int size) {
  int max = arr[0];
  for(int i = 1; i < size; i++) {
    if(arr[i] > max)
      max = arr[i];
  }
  return &max;
}

int main() {
  int numbers[] = {5, 2, 9, 1, 7};
  int* maxPtr = findMax(numbers, 5);
  printf("Max: %d", *maxPtr);
  return 0;
}`,
      solution: `#include <stdio.h>
#include <stdlib.h>

int* findMax(int arr[], int size) {
  int* max = malloc(sizeof(int));
  *max = arr[0];
  for(int i = 1; i < size; i++) {
    if(arr[i] > *max)
      *max = arr[i];
  }
  return max;
}

int main() {
  int numbers[] = {5, 2, 9, 1, 7};
  int* maxPtr = findMax(numbers, 5);
  printf("Max: %d", *maxPtr);
  free(maxPtr);
  return 0;
}`,
      hint: "You're returning the address of a local variable. Think about where that variable lives in memory!",
    }
  ],
}; 