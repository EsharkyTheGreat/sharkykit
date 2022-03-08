import pwn
import time


class BufferOverflow():

    def __init__(self, elf: pwn.ELF) -> None:
        self.elf = elf

    def create_proc(self, aslr=True):
        if self.elf:
            self.process = pwn.process(self.elf.path, aslr=aslr)
        else:
            pwn.log.error("Error No ELF file present")

    def get_offset_ret(self, vuln_func=None):
        if vuln_func:
            self.process = vuln_func(self.process)
        proc = self.process
        proc.sendline(pwn.cyclic(0x1000))
        proc.wait()
        time.sleep(2)
        core_file = proc.corefile
        fault_addr = core_file.fault_addr
        self.offset = pwn.cyclic_find(fault_addr & 0xffffffff)
        proc.close()
