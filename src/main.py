import sharkykit
import pwn

elf = pwn.context.binary = pwn.ELF(
    "./tests/bof32ret2shellcode/bof32ret2shellcode")
bof = sharkykit.bof(elf)
bof.createProc(aslr=False)