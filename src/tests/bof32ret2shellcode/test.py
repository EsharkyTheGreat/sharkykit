import sharkykit
import pwn

elf = pwn.context.binary = pwn.ELF("./bof32ret2shellcode")
bof = sharkykit.bof(elf)
bof.create_proc(aslr=False)
bof.get_offset_ret()
print(bof.offset)