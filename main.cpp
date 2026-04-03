#include <iostream>
#include <print>

struct foo_t {
  int a, b;
};
struct bar_t {
  foo_t x, y;
};
struct arr_t {
  int* v;
  int size;
};

int main(int argc, char** argv) {
  std::println("hello, world");

  foo_t f = {.a = 30, .b = 25};
  foo_t f2 = {.a = 12, .b = 123};
  bar_t b = {.x = f, .y = f2};

  foo_t fs[20] = {};
  fs[0] = f;
  fs[1] = f2;

  arr_t arr;
  arr.v = new int[10];
  arr.size = 10;

  for (int i = 0; i < 10; i++) {
    arr.v[i] = i;
  }

  return 0;
}
