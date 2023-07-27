#!/bin/bash

# number=20

# if [ $number -eq 20 ]; then
#     echo "George to start with kahoot"
#     echo "Jit will start with caffeine"
#     echo "Akash will start with class"
# else
#     echo "Wait for students to come"
# fi

# fruits=("apple" "mango" "banana")

# for fruit in "${fruits[@]}"; do
#     echo $fruit is tasty
# done

if command -v python &> /dev/null; then
    echo "Python found terminal app now executing"
else
    echo "missing python"
fi
