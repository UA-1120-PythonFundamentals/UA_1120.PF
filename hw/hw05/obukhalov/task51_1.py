#!/usr/bin/env pyton


def main():
    int_list = [1, 2, 3, 4, 5]
    float_list = []

    for i in int_list:
        float_list.append(float(i))

    print(f"Integer numbers list: {int_list}")
    print(f"Floating numbers list: {float_list}")


if __name__ == "__main__":
    main()
