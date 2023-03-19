#!/bin/bash

# Read integer input
read -p "Enter an integer: " m

# Check integer if even
if ((m % 2 == 0)); then
    echo "Weird"
else
    # Check if odd and in the  range of 2 to 5
    if ((m >= 2 && m <= 5)); then
        echo "Not Weird"
    # Check if odd and in the range of 6 to 20
    elif ((m >= 6 && m <= 20)); then
        echo "Weird"
    # Check if the integer is odd and greater than 20
    else
        echo "Not Weird"
    fi
fi
