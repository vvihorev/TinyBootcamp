#include <stdio.h>


int main() {
  for (long a = 3; a < 151; a++) {
    for (long b = 3; b < 151; b++) {
      for (long c = 3; c < 151; c++) {
        for (long d = 3; d < 151; d++) {
          for (long e = 3; e < 151; e++) {
            if (a*a*a*a*a + b*b*b*b*b + c*c*c*c*c + d*d*d*d*d == e*e*e*e*e) {
              printf("%li, %li, %li, %li, %li", a, b, c, d, e);
              return 0;
            }
          }
        }
      }
    }
  }
}

