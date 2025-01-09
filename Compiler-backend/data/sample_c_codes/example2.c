// example2.c

int add(int a, int b) {
    return a + b;
}

int main() {
    int x = 5;
    int y = 10;
    float z = add(x, y) * 2.5;
    if (z > 20.0) {
        return 1;
    } else {
        return 0;
    }
}
