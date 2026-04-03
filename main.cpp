#include <iostream>
#include <print>

struct foo {
  int a, b;
};
struct bar {
  struct foo x, y;
};

int main(int argc, char** argv) {
  std::println("hello, world");

  foo f = {.a = 30, .b = 25};
  foo f2 = {.a = 12, .b = 123};
  bar b = {.x = f, .y = f2};

  return 0;
}
