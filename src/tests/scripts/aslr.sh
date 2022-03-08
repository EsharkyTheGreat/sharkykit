#!/bin/bash
if [[ $1 == 'enable' ]]; then
    echo "[*] You are enabling ASLR!"
    echo 2 | sudo tee /proc/sys/kernel/randomize_va_space
elif [[ $1 == 'disable' ]]; then
    echo "[*] You are disabling ASLR!"
    echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
else
    echo "[!] Invalid Option"
fi